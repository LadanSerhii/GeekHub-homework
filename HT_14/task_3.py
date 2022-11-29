# 3. http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про записи: цитата, автор,
# інфа про автора тощо.
# - збирається інформація з 10 сторінок сайту.
# - зберігати зібрані дані у CSV файл

import requests
from bs4 import BeautifulSoup
import csv
from dataclasses import dataclass
from dataclasses import fields
from dataclasses import astuple


@dataclass
class Quote(object):

    quote: str
    author: str
    author_info: str
    tags: str


class SiteParser(object):
    BASE_URL = 'http://quotes.toscrape.com'
    FILE_PATH = 'results.csv'
    QUOTE_FIELDS = [field.name for field in fields(Quote)]

    def site_parse(self) -> [Quote]:
        print(f'=== Parsing on the page 1 ===')
        page = requests.get(self.BASE_URL)
        soup = BeautifulSoup(page.content, 'lxml')
        results = self.page_parse(soup)
        for page_number in range(2, 11):
            print(f'=== Parsing on the page {page_number} ===')
            page = requests.get(self.BASE_URL + '/page/' + str(page_number) + '/')
            soup = BeautifulSoup(page.content, 'lxml')
            results.extend(self.page_parse(soup))
        return results

    def page_parse(self, soup) -> [Quote]:
        data = soup.select('div.quote')
        results = []
        for element in data:
            results.append(self.quote_parse(element))
        return results

    def quote_parse(self, quote_soup: BeautifulSoup) -> [Quote]:
        print('=== Start quote parse ===')
        quote = quote_soup.select_one('.text').text
        author = quote_soup.select_one('.author').text
        author_url = quote_soup.select_one('a').get('href')
        author_info = self.author_description_parse(author_url)
        tg = quote_soup.select('.tag')
        tags = ''
        for tag in tg:
            tags += tag.text + ', '
        # print(quote)
        # print(author)
        # print(tags)
        # print(author_info)
        return Quote(
            quote=quote,
            author=author,
            author_info=author_info,
            tags=tags[:-2]
        )

    def author_description_parse(self, author_url):
        page = requests.get(self.BASE_URL + author_url)
        soup_author = BeautifulSoup(page.content, 'lxml')
        author_description = soup_author.select_one('.author-description').text.replace("    ", "").replace('\n', '')
        return author_description

    def data_to_csv(self, results: [Quote]):
        with open(self.FILE_PATH, 'w', encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.QUOTE_FIELDS)
            for result in results:
                writer.writerow(astuple(result))
        return

    def print_results(self, results: [Quote]):
        for result in results:
            print(astuple(result))


if __name__ == '__main__':
    site = SiteParser()
    results = site.site_parse()
    site.data_to_csv(results)


