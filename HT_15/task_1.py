# 1. Викорисовуючи requests/BeautifulSoup, заходите на ось цей сайт "https://www.expireddomains.net/domain-lists/"
# (з ним будьте обережні :wink::skull_and_crossbones:), вибираєте будь-яку на ваш вибір доменну зону і парсите список
# доменів з усіма відповідними колонками - доменів там буде десятки тисяч (звичайно ураховуючи пагінацію).
# Всі отримані значення зберегти в CSV файл.

import requests
from bs4 import BeautifulSoup
import csv
import random
import time


class SiteParser(object):
    BASE_URL = 'https://www.expireddomains.net/godaddy-closeout-domains/'
    OTHER_URL = 'https://www.w3schools.com/cssref/css_selectors.php'
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
        rnd = random.randint(0, len(self.user_agents) - 1)
        self.headers['User-Agent'] = self.user_agents[rnd]
        self.headers['Accept'] = self.accept
        self.headers['Accept-Encoding'] = self.accept_encoding
        rnd = random.randint(0, len(self.accept_languages) - 1)
        self.headers['Accept-Language'] = self.accept_languages[rnd]
        rnd_time = random.randint(0, 5)
        time.sleep(rnd_time)
        return self.headers

    def site_parse(self):
        dct = dict()
        lst = []
        session = requests.Session()
        for page in range(12):
            if not page:
                result = session.get(self.BASE_URL, headers=self.headers_make())
            else:
                result = session.get(self.BASE_URL + '?start=' + str(page * 25) + '#listing',
                                     headers=self.headers_make())
            soup = BeautifulSoup(result.content, 'lxml')
            data = soup.select('tbody tr')
            for el in data:
                dct['domain'] = el.select_one('td.field_domain').text
                dct['bl'] = el.select_one('td.field_bl').text
                dct['domainpop'] = el.select_one('td.field_domainpop').text
                dct['abirth'] = el.select_one('td.field_abirth').text
                dct['aentries'] = el.select_one('td.field_aentries').text
                dct['dmoz'] = el.select_one('td.field_dmoz').text
                dct['statuscom'] = el.select_one('td.field_statuscom').text
                dct['statusnet'] = el.select_one('td.field_statusnet').text
                dct['statusorg'] = el.select_one('td.field_statusorg').text
                dct['statusde'] = el.select_one('td.field_statusde').text
                dct['statustld_registered'] = el.select_one('td.field_statustld_registered').text
                dct['traffic'] = el.select_one('td.field_traffic').text
                dct['valuation'] = el.select_one('td.field_valuation').text
                dct['price'] = el.select_one('td.field_price').text
                lst.append(dct.copy())
                print(f'{len(lst)} URLs parsed and added to file!')
                dct.clear()
        return lst

    def save_to_csv(self, results):
        with open(self.FILE_PATH, 'w', encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(results[0].keys())
            for result in results:
                writer.writerow(result.values())


if __name__ == '__main__':
    site = SiteParser()
    site.save_to_csv(site.site_parse())


