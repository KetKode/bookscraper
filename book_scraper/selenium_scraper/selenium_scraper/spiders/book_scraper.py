import scrapy
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


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

            yield response.follow(url=url, callback=self.parse_book, meta={'book_data': book_data})

    def parse_book(self, response):
        book_data = response.meta['book_data']

        cover_url = response.css('.BookPage__bookCover .ResponsiveImage::attr(src)').extract_first()
        rating_small = response.css('.RatingStatistics__interactive .RatingStatistics__rating::text').extract_first()
        genres = response.css('.BookPageMetadataSection__genreButton .Button__labelItem::text').extract()


        # summary_open = self.driver.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "BookPageMetadataSection__description", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "Button__labelItem", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]')
        # summary_open.click()
        #
        # summary = response.css('.TruncatedContent__text--large .DetailsLayoutRightParagraph__widthConstrained::text').extract_first()


        # book_data['summary'] = summary
        book_data['cover_url'] = cover_url
        book_data['rating_small'] = rating_small
        # book_data['summary'] = summary
        book_data['genres'] = genres

        yield book_data

        # next_page = response.css(".pagination .next_page::attr(href)").get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)

    # def parse_each_book(self, response):
    #
    #
    #     summary = response.css(".TruncatedContent__text--expanded .DetailsLayoutRightParagraph__widthConstrained::text").extract_first()
    #
    #     summary = {
    #         "summary": summary,
    #         }
    #
    #     yield summary
