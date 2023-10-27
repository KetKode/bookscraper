# bookscraper 📖
**Scraper collecting data from Goodreads.**

In this code I'm scraping through a list of books published on Goodreads, collect **url, title, rating**.
Spider also collects **summary and cover, genres, buy links, number of pages** from each book's page.
There is additional script to calculate estimated amount of time needed to finish the book.
It iterates through all pages (100) until there is no more next page.

By running 
```
scrapy crawl book_scraper -o <create any file name>.csv
```

you will get your data in a csv file.

I'm using this scraper as a part of a bigger project, where I need a lot of book data.
