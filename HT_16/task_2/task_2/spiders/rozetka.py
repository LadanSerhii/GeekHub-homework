import scrapy


class RozetkaSpider(scrapy.Spider):
    name = 'rozetka'
    category = 'mobile-phones'
    category_code = 'c80003'
    allowed_domains = ['rozetka.com.ua']
    custom_settings = {
        'FEEDS': {f'{category_code}.csv': {'format': 'csv', }}
    }

    def start_requests(self):
        urls = [
            'https://rozetka.com.ua/ua/mobile-phones/' + self.category_code + '/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for unit in response.css('div.goods-tile__inner'):
            category = self.category
            product = unit.css('span.goods-tile__title::text').get().strip()
            if 'Мобільний телефон' in product:
                brand = product.split(' ')[2]
            elif 'Смартфон' in product:
                brand = product.split(' ')[1]
            else:
                brand = 'No Brand'
            price = unit.css('span.goods-tile__price-value::text').get().replace(u'\xa0', '').replace(' ', '')
            rank = unit.css('stop::attr(offset)').get()
            yield {
                'Category': category,
                'Product': product,
                'Brand': brand,
                'Price': price,
                'Rank': rank,
            }
        next_page = response.css('a.pagination__direction--forward::attr(href)').get()
        print(f'Next page parse')
        if next_page:
            yield response.follow(next_page, callback=self.parse)