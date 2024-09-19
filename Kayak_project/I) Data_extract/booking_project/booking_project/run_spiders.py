from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.scrapy_booking import ScrapingBooking  # Import de votre premier spider

if __name__ == "__main__":
    # Obtenir les paramètres du projet Scrapy
    process = CrawlerProcess(get_project_settings())

    # Ajouter chaque spider que vous souhaitez exécuter
    process.crawl(ScrapingBooking)


    # Démarrer les spiders
    process.start()