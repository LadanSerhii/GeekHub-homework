# 1. Викорисовуючи requests/BeautifulSoup, заходите на ось цей сайт "https://www.expireddomains.net/domain-lists/"
# (з ним будьте обережні :wink::skull_and_crossbones:), вибираєте будь-яку на ваш вибір доменну зону і парсите список
# доменів з усіма відповідними колонками - доменів там буде десятки тисяч (звичайно ураховуючи пагінацію).
# Всі отримані значення зберегти в CSV файл.

import csv
import random
import time
from bs4 import BeautifulSoup
import requests


class SiteParser(object):
    BASE_URL = 'https://www.expireddomains.net/godaddy-closeout-domains/'
    FILE_PATH = 'domains.csv'
    headers = dict()
    user_agents = [
        'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Version/4.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 9; SM-G973U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/69.0.3497.100 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/52.0.2743.98 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/52.0.2743.98 Mobile Safari/537.36'
    ]
    accept_languages = [
        'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
        'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5',
        'en-US,en;q=0.5',
        'de-CH',
        'en-ca,en;q=0.8,en-us;q=0.6,de-de;q=0.4,de;q=0.2'
    ]
    accept = 'application/json,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    accept_encoding = 'gzip, deflate, sdch'

    def headers_make(self):
        self.headers['User-Agent'] = self.user_agents[random.randint(0, len(self.user_agents) - 1)]
        self.headers['Accept'] = self.accept
        self.headers['Accept-Encoding'] = self.accept_encoding
        self.headers['Accept-Language'] = self.accept_languages[random.randint(0, len(self.accept_languages) - 1)]

        return self.headers

    def site_parse(self):
        domain_data = dict()
        domain_list = []
        session = requests.Session()
        for page in range(12):
            time.sleep(random.randint(0, 5))
            if not page:
                result = session.get(self.BASE_URL, headers=self.headers_make())
            else:
                result = session.get(self.BASE_URL + '?start=' + str(page * 25) + '#listing',
                                     headers=self.headers_make())
            soup = BeautifulSoup(result.content, 'lxml')
            data = soup.select('tbody tr')
            for el in data:
                domain_data['domain'] = el.select_one('td.field_domain').text
                domain_data['bl'] = el.select_one('td.field_bl').text
                domain_data['domainpop'] = el.select_one('td.field_domainpop').text
                domain_data['abirth'] = el.select_one('td.field_abirth').text
                domain_data['aentries'] = el.select_one('td.field_aentries').text
                domain_data['dmoz'] = el.select_one('td.field_dmoz').text
                domain_data['statuscom'] = el.select_one('td.field_statuscom').text
                domain_data['statusnet'] = el.select_one('td.field_statusnet').text
                domain_data['statusorg'] = el.select_one('td.field_statusorg').text
                domain_data['statusde'] = el.select_one('td.field_statusde').text
                domain_data['statustld_registered'] = el.select_one('td.field_statustld_registered').text
                domain_data['traffic'] = el.select_one('td.field_traffic').text
                domain_data['valuation'] = el.select_one('td.field_valuation').text
                domain_data['price'] = el.select_one('td.field_price').text
                domain_list.append(domain_data.copy())
                print(f'{len(domain_list)} URLs parsed and added to file!')
                domain_data.clear()
        return domain_list

    def save_to_csv(self, results):
        with open(self.FILE_PATH, 'w', encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(results[0].keys())
            for result in results:
                writer.writerow(result.values())


if __name__ == '__main__':
    site = SiteParser()
    site.save_to_csv(site.site_parse())


