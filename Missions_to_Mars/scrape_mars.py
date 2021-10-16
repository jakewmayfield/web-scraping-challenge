# Dependenciespip
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
    
    # Retrieve the latest news title and paragraph
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html=browser.html
    soup=bs(html,'html.parser')
    news_title=soup.find_all('div', class_='content_title')[0].text
    news_p=soup.find_all('div', class_='article_teaser_body')[0].text

    # Retrieve Mars photo
    photo_url = 'https://spaceimages-mars.com'
    browser.visit(photo_url)
    html2=browser.html
    soup2=bs(html2,'html.parser')
    mars=soup2.find_all("a", class_="fancybox-thumbs")[0]["href"]
    featured_image_url = photo_url+"/"+mars

    # Retrieve Mars facts
    facts_url = 'https://galaxyfacts-mars.com'
    browser.visit(facts_url)
    html3=browser.html
    soup3=bs(html3,'html.parser')
    tables=pd.read_html(facts_url)
    mars_facts=tables[1]
    mars_facts=mars_facts.rename(columns={0:"Measurement", 1:"Value"}).set_index("Measurement")
    fact_table=mars_facts.to_html().replace("\n","")

    # Retrieve hemisphere info
    hemis_url = 'https://marshemispheres.com/'
    browser.visit(hemis_url)
    html4=browser.html
    soup4=bs(html4,'html.parser')
    mars_links = soup4.find('div', class_='collapsible results')
    mars_hemis = mars_links.find_all('div', class_='item')
    hemisphere_image_urls=[]

    for item in mars_hemis:
        # Extract title
        hem=item.find('div',class_='description')
        title=hem.h3.text
        # Extract image url
        hem_url=hem.a['href']
        browser.visit(hemis_url+hem_url)
        html=browser.html
        soup=bs(html,'html.parser')
        image_url=soup.find('li').a['href']
        image_src=(hemis_url+image_url)
        # Create dictionary for title and url
        hem_dict={
            'title':title,
            'image_url':image_src
        }
        hemisphere_image_urls.append(hem_dict)

        mars_dict={
            "news_title":news_title,
            "news_p":news_p,
            "featured_image_url":featured_image_url,
            "fact_table":fact_table,
            "hemisphere_images":hemisphere_image_urls
        }

    browser.quit()
    return mars_dict





