import scrapy
from scrapy_selenium import SeleniumRequest


class BookScraperSpider(scrapy.Spider):
    name = "book_scraper"

    def start_requests(self):
        url = "https://www.goodreads.com/list/show/1.Best_Books_Ever"
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        for book in response.xpath('//tr[@itemscope and @itemtype="http://schema.org/Book"]'):
            title = book.css(".bookTitle span::text").extract_first()
            author = book.css(".authorName span::text").extract_first()
            rating = book.css(".minirating::text").extract_first()
            url = book.css('.bookTitle::attr(href)').extract_first()

            book_data = {
                "title": title,
                "author": author,
                "rating": rating,
                "url": "https://www.goodreads.com" + url
                }

            yield book_data
