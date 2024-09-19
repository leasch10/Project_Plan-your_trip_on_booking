# Import os => Library used to easily manipulate operating systems
## More info => https://docs.python.org/3/library/os.html
import os 

# Import logging => Library used for logs manipulation 
## More info => https://docs.python.org/3/library/logging.html
import logging

# Import scrapy and scrapy.crawler 
import scrapy
from scrapy.crawler import CrawlerProcess


class ScrapingBooking(scrapy.Spider):
    # Name of your spider
    name = "scraping_booking"

    # Url to start your spider from 
    start_urls = [
        'https://www.booking.com/searchresults.en-gb.html?ss=Ch%C3%A2teau+du+Haut-K%C5%93nigsbourg&ssne=S%C3%A9lestat&ssne_untouched=S%C3%A9lestat&label=en-fr-booking-desktop-Akb7DsuMl_04Kj1fagYeEgS652796016858%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1006094%3Ali%3Adec%3Adm&sid=f2480d4adff900632cc88bb076d858c9&aid=2311236&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=5865396&dest_type=hotel&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=4&search_selected=true&search_pageview_id=bcd1722f7e4707b4&ac_meta=GhBiY2QxNzIyZjdlNDcwN2I0IAAoATICZW46HUNow6J0ZWF1IGR1IEhhdXQtS8WTbmlnc2JvdXJnQABKAFAA&checkin=2024-09-18&checkout=2024-09-19&group_adults=2&no_rooms=1&group_children=0',
        'https://www.booking.com/searchresults.en-gb.html?label=en-fr-booking-desktop-Akb7DsuMl_04Kj1fagYeEgS652796016858%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1006094%3Ali%3Adec%3Adm&sid=f2480d4adff900632cc88bb076d858c9&aid=2311236&ss=Gorges+du+Verdon&ssne=Collioure&ssne_untouched=Collioure&lang=en-gb&src=searchresults&dest_id=2746&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=c826428873311082&checkin=2024-09-18&checkout=2024-09-19&group_adults=2&no_rooms=1&group_children=0&nflt=ht_id%3D204',
        'https://www.booking.com/searchresults.en-gb.html?label=en-fr-booking-desktop-Akb7DsuMl_04Kj1fagYeEgS652796016858%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1006094%3Ali%3Adec%3Adm&sid=f2480d4adff900632cc88bb076d858c9&aid=2311236&ss=Annecy&ssne=Gorges+du+Verdon&ssne_untouched=Gorges+du+Verdon&lang=en-gb&src=searchresults&dest_id=-1407760&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=c8264292cb7b08e0&checkin=2024-09-18&checkout=2024-09-19&group_adults=2&no_rooms=1&group_children=0&nflt=ht_id%3D204',
        'https://www.booking.com/searchresults.en-gb.html?label=en-fr-booking-desktop-Akb7DsuMl_04Kj1fagYeEgS652796016858%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1006094%3Ali%3Adec%3Adm&sid=f2480d4adff900632cc88bb076d858c9&aid=2311236&ss=Besan%C3%A7on&ssne=Annecy&ssne_untouched=Annecy&lang=en-gb&src=searchresults&dest_id=-1412198&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=b49142a4a35507f8&checkin=2024-09-18&checkout=2024-09-19&group_adults=2&no_rooms=1&group_children=0&nflt=ht_id%3D204',
        'https://www.booking.com/searchresults.html?label=en-fr-booking-desktop-Akb7DsuMl_04Kj1fagYeEgS652796016858%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1006094%3Ali%3Adec%3Adm&sid=f2480d4adff900632cc88bb076d858c9&aid=2311236&ss=Le+Mont+Saint+Michel%2C+Lower+Normandy%2C+France&ssne=S%C3%A9lestat&ssne_untouched=S%C3%A9lestat&lang=en-us&src=searchresults&dest_id=900039327&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=229b5487234e0161&checkin=2024-09-18&checkout=2024-09-19&group_adults=2&no_rooms=1&group_children=0&nflt=ht_id%3D204',
    ]

    # Callback function that will be called when starting your spider
    # It will get text, author and tags of the first <div> with class="quote"
    def parse(self, response):
        #quote = response.css("div.quote")
        hotels = response.xpath("/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[3]/div")
        for hotel in hotels:
            name = hotel.css('div.f6431b446c.a15b38c233::text').get()
            if name:
                yield {
                    'city':response.css('span.aee5343fdb.def9bc142a::text').get(),
                    'name':name,
                    'url':hotel.css("a.a78ca197d0::attr(href)").get(),
                    "rating":hotel.css("div.a3b8729ab1.d86cee9b25 div.ac4a7896c7::text").get().strip(" ").split()[1]
                }

# Name of the file where the results will be saved
filename = "booking_test.json"

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
process.crawl(ScrapingBooking)
process.start()