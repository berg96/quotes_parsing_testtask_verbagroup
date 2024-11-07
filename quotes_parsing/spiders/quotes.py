import scrapy

from quotes_parsing.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield QuoteItem(
                text=quote.css('span.text::text').get(),
                author=quote.css('small.author::text').get(),
                tags=quote.css('a.tag::text').getall(),
            )

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
