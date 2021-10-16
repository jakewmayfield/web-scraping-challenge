# web-scraping-challenge
In this assignment, I build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

## Step 1 - Scraping

### NASA Mars News

* Scrape https://redplanetscience.com/ and collect the latest News Title and Paragraph Text.

### JPL Mars Space Images - Featured Image

* Visit https://spaceimages-mars.com

* Use splinter to navigate the site and find the image url for the current Featured Mars Image

* Make sure to find the image url to the full size `.jpg` image.

* Make sure to save a complete url string for this image.

### Mars Facts

* Visit https://galaxyfacts-mars.com and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Use Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* Visit https://marshemispheres.com/ to obtain high resolution images for each of Mar's hemispheres.

* You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.

* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data.

* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


## Step 2 - MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Convert Jupyter notebook into a Python script that will execute all of the scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, create a route called `/scrape` that will import `scrape_mars.py` script

  * Store the return value in Mongo as a Python dictionary.

* Create a root route `/` that will query Mongo database and pass the mars data into an HTML template to display the data.

* Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements.