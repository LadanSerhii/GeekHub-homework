import scrapy
import xmltodict


class ChromeSpider(scrapy.Spider):
    name = 'chrome'
    allowed_domains = ['chrome.google.com']
    custom_settings = {
        'FEEDS': {'chrome_extensions.csv': {'format': 'csv', }}
    }

    def start_requests(self):
        urls = [
            'https://chrome.google.com/webstore/sitemap',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        '''Parse first XML page'''
        data = xmltodict.parse(response.body)
        xml_urls = []
        for element in data.get('sitemapindex').get('sitemap'):
            xml_urls.append(element.get('loc'))
        for url in xml_urls:
            yield scrapy.Request(response.urljoin(url), callback=self.parse_loc)

    def parse_loc(self, response):
        '''Parse <loc> pages'''
        data = xmltodict.parse(response.body)
        links = []
        for element in data.get('urlset').get('url'):
            links.append(element.get('loc'))
        for link in links:
            yield scrapy.Request(response.urljoin(link), callback=self.parse_page)

    '''Parse extension pages'''
    def parse_page(self, response):
        data = response.css('html')
        for page in data:
            extension_id = page.css('head link::attr(href)').getall()[-1].split('/')[-1].split('?')[0]
            name = page.css('h1.e-f-w::text').get()
            description = page.css('div.C-b-p-j-Pb::text').get()
            yield {
                'ID': extension_id,
                'Name': name,
                'Description': description,
            }