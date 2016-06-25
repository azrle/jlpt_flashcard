import scrapy

from jlpt_flashcard.items import JlptFlashcardItem

class JlptFlashCardSpider(scrapy.Spider):
    name = 'grammar'
    start_urls = [
        'http://japanesetest4you.com/jlpt-n3-grammar-list/',
        'http://japanesetest4you.com/jlpt-n2-grammar-list/',
    ]

    def parse(self, response):
        for url in response.css('a::attr("href")').re('.*/flashcard/learn.*'):
            yield scrapy.Request(response.urljoin(url), self.parse_item)

    def parse_item(self, response):
        item = JlptFlashcardItem()
        for post_title in response.css('h2.title::text').extract():
            item['title'] = post_title
        for flashcard in response.css('img::attr("src")').re('.*/flashcard/wp-content/.*'):
            item['link'] = flashcard
        yield item
