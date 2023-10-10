# bookscraping 📖
**Scraper collecting data from Goodreads.**

In this code I'm scraping through a list of books published on Goodreads, collect **url, title, rating**.
Spider also collects **summary and cover** from each book's page (10.000 in total)
It iterates through all pages (100) until there is no more next page.

By running 
```
scrapy crawl book_scraper -o <your file name>.csv
```

you will get your data in a csv file.

I'm using this scraper as a part of a bigger project, where I need a lot of book data.
