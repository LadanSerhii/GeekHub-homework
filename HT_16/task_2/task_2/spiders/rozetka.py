import scrapy


class RozetkaSpider(scrapy.Spider):
    name = 'rozetka'
    category = 'mobile-phones'
    category_code = 'c80003'
    base_url = 'https://rozetka.com.ua/ua/'
    allowed_domains = ['rozetka.com.ua']
    custom_settings = {
        'FEEDS': {f'{category_code}.csv': {'format': 'csv', }}
    }

    def start_requests(self):
        urls = [
            self.base_url + self.category + '/' + self.category_code + '/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        '''Parse category page'''
        page_number = response.css('a.pagination__link::text').getall()[-1]
        page_number = int(page_number)
        for page in range(1, page_number + 1):
            url = self.base_url + self.category + '/' + self.category_code + '/' + f'page={page}' + '/'
            yield scrapy.Request(response.urljoin(url), callback=self.parse_category_page)

    def parse_category_page(self, response):
        '''Parse products in category page'''
        product_pages = response.css('a.goods-tile__heading::attr(href)').getall()
        for product_page in product_pages:
            yield scrapy.Request(response.urljoin(product_page), callback=self.parse_product)

    def parse_product(self, response):
        '''Parse product'''
        category = response.css('a.breadcrumbs__link span::text').getall()[-2]
        brand = response.css('a.breadcrumbs__link span::text').getall()[-1].replace(category + ' ', '')
        model = response.css('h1.product__title::text').get().strip()
        price = response.css('p.product-prices__big::text').get().replace(u'\xa0', '').replace(' ', '')
        rank_list = response.css('div.product__rating stop::attr(offset)').getall()

        if rank_list:
            rank = 0
            for index in range(0, len(rank_list), 2):
                rank += 0.2 * float(rank_list[index])
            if rank != 0:
                rank = round(rank, 4)
            else:
                rank = 'No Rank'
        yield {
            'Category': category,
            'Brand': brand,
            'Model': model,
            'Price': price,
            'Rank': rank,
        }