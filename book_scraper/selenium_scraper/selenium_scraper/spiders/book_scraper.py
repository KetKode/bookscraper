import scrapy
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
import re
import json
import datetime


class BookScraperSpider(scrapy.Spider):
    name = "book_scraper"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def start_requests(self):
        url = "https://www.goodreads.com/list/show/43.Best_Young_Adult_Books"
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        for book in response.xpath('//tr[@itemscope and @itemtype="http://schema.org/Book"]'):
            title = book.css(".bookTitle span::text").extract_first()
            author = book.css(".authorName span::text").extract_first()
            url = book.css('.bookTitle::attr(href)').extract_first()

            book_data = {
                "title": title,
                "author": author,
                "url": "https://www.goodreads.com" + url
                }

            # next_page = response.css(".pagination .next_page::attr(href)").get()
            # if next_page is not None:
            #     yield response.follow(next_page, callback=self.parse)

            yield response.follow(url=url, callback=self.parse_book, meta={'book_data': book_data})

    def parse_book(self, response):
        book_data = response.meta['book_data']

        cover_url = response.css('.BookPage__bookCover .ResponsiveImage::attr(src)').extract_first()
        rating = response.css('.RatingStatistics__interactive .RatingStatistics__rating::text').extract_first()
        genres = response.css('.BookPageMetadataSection__genreButton .Button__labelItem::text').extract()

        summary_tags = response.css('[data-testid="description"]').get()
        summary = re.sub(r'<.*?>', '', summary_tags)

        pages_text = response.css('p[data-testid="pagesFormat"]::text').get()
        pages_pattern = r'(\d+)\s+pages'
        pages_match = re.search(pages_pattern, pages_text)
        if pages_match:
            number_of_pages = int(pages_match.group(1))
            time_to_finish = (number_of_pages * 2) / 60

            time = f"{int (time_to_finish)} hours {int ((time_to_finish * 60) % 60)} minutes"

        amazon_link = None

        script_content = response.css('script#__NEXT_DATA__::text').extract_first()
        data = json.loads(script_content)

        apollo_state = data.get("props", {}).get("pageProps", {}).get("apolloState", {})

        book_key = None
        for key in apollo_state:
            if "Book" in key:
                book_key = key
                break

        if book_key:
            # Extract the 'id' field from the found book key
            book_id = apollo_state[book_key].get("id")
            book_key = f"Book:" + book_id
            amazon_link = apollo_state.get(book_key, {}).get('links({})', {}).get('primaryAffiliateLink', {}).get("url")

            audible_link = apollo_state.get(book_key, {}).get('links({})', {}).get('secondaryAffiliateLinks')[0].get("url")

            year_release = apollo_state.get(book_key, {}).get('details', {}).get("publicationTime")

            format_book = apollo_state.get(book_key, {}).get('details', {}).get("format")
            language = apollo_state.get(book_key, {}).get('details', {}).get('language', {}).get("name")
            isbn = apollo_state.get(book_key, {}).get('details', {}).get("isbn")
            isbn13 = apollo_state.get(book_key, {}).get('details', {}).get("isbn13")



        # print ("Data:", data)
        # props = data.get ("props", {})
        # print ("Props:", props)
        # page_props = props.get ("pageProps", {})
        # print ("Page Props:", page_props)
        # apollo_state = page_props.get ("apolloState", {})
        # print ("Apollo State:", apollo_state)
        # links_data = apollo_state.get ("links({})", {})
        # print ("Links Data:", links_data)
        #
        # for key, value in apollo_state.items ():
        #     if "primaryAffiliateLink" in value:
        #         amazon_link = value["primaryAffiliateLink"].get ("url")
        #         break

        # Access the Amazon link data

        book_data['cover_url'] = cover_url
        book_data['rating'] = rating
        book_data['summary'] = summary
        book_data['genres'] = genres
        book_data['number_of_pages'] = number_of_pages
        book_data['time'] = time
        book_data['amazon_link'] = amazon_link
        book_data['audible_link'] = audible_link
        book_data['year_release'] = year_release
        book_data['format_book'] = format_book
        book_data['language'] = language
        book_data['isbn'] = isbn
        book_data['isbn13'] = isbn13

        yield book_data


