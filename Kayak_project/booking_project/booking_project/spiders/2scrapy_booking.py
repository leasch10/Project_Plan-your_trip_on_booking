# Import os => Library used to easily manipulate operating systems
## More info => https://docs.python.org/3/library/os.html
import os 

# Import logging => Library used for logs manipulation 
## More info => https://docs.python.org/3/library/logging.html
import logging

# Import scrapy and scrapy.crawler 
import scrapy
from scrapy.crawler import CrawlerProcess

 #ouvrir le fichier url 
path = "c:\\Users\\leasc\\github\\data_management_collection-\\Kayak_project/booking_project/booking_project/url_list"
with open(path, "r") as infile:
    urls=infile.readlines()

class SearchPage(scrapy.Spider):
    # Name of your spider
    name = "search_page"

    # Starting URL
    start_urls = urls

    # Parse function for login
    def parse(self, response):
        
        yield {
            'name': response.css("h2.d2fee87262::text").get(),
            'latitude' : response.xpath('//a[@id="hotel_address"]/@data-atlas-bbox').get().split(",")[0],
            'longitude':response.xpath('//a[@id="hotel_address"]/@data-atlas-bbox').get().split(",")[1],
            'latitude2':response.xpath('//a[@id="hotel_address"]/@data-atlas-latlng').get().split(",")[0],
            'longitude2':response.xpath('//a[@id="hotel_address"]/@data-atlas-latlng').get().split(",")[1],
            'description':response.css('p[data-testid= "property-description"]::text').get()
                }
filename = "booking_test2.json"

# If file already exists, delete it before crawling (because Scrapy will 
# concatenate the last and new results otherwise)
if filename in os.listdir('booking_project/'):
        os.remove('booking_project/' + filename)

# Declare a new CrawlerProcess with some settings
## USER_AGENT => Simulates a browser on an OS
## LOG_LEVEL => Minimal Level of Log 
## FEEDS => Where the file will be stored 
## More info on built-in settings => https://docs.scrapy.org/en/latest/topics/settings.html?highlight=settings#settings
process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        'booking_project/' + filename : {"format": "json"},
    }
})

# Start the crawling using the spider you defined above
process.crawl(SearchPage)
process.start()