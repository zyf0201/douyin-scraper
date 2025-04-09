import scrapy
from scrapy.crawler import CrawlerProcess
from scraper.spiders.example_spider import ExampleSpider

def main():
    process = CrawlerProcess()
    process.crawl(ExampleSpider)
    process.start()

if __name__ == "__main__":
    main()