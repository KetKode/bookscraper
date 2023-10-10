import scrapy
from scrapy_selenium import SeleniumRequest
from selenium import webdriver


class BookScraperSpider(scrapy.Spider):
    name = "book_scraper"

    def __init__(self):
        self.driver = webdriver.Chrome()

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

            next_page = response.css(".pagination .next_page::attr(href)").get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)

            yield response.follow(url=url, callback=self.parse_book, meta={'book_data': book_data})

    def parse_book(self, response):
        book_data = response.meta['book_data']

        cover_url = response.css('.BookPage__bookCover .ResponsiveImage::attr(src)').extract_first()
        rating_small = response.css('.RatingStatistics__interactive .RatingStatistics__rating::text').extract_first()
        genres = response.css('.BookPageMetadataSection__genreButton .Button__labelItem::text').extract()
        summary = response.css('.TruncatedContent__text--large .DetailsLayoutRightParagraph__widthConstrained .Formatted::text').extract_first()

        book_data['cover_url'] = cover_url
        book_data['rating_small'] = rating_small
        book_data['summary'] = summary
        book_data['genres'] = genres

        yield book_data


