# 2. Створіть програму для отримання курсу валют за певний період.
# - отримати від користувача дату (це може бути як один день так і інтервал - початкова і кінцева дати, продумайте
# механізм реалізації) і назву валюти
# - вивести курс по відношенню до гривні на момент вказаної дати (або за кожен день у вказаному інтервалі)
# - не забудьте перевірку на валідність введених даних

import requests
from bs4 import BeautifulSoup
import json
import urllib
from datetime import datetime


class SiteRequest(object):
    FOR_CURR_LIST = 'https://bank.gov.ua/NBU_Exchange/exchange_site?start=yyyymmdd&end=%20yyyymmdd&valcode=&sort=exchangedate&order=desc&json'
    url_to_get = 'https://bank.gov.ua/NBU_Exchange/exchange_site?start=_date_start_to_change_&end=%20_date_end_to_change_&valcode=_code_to_change_&sort=exchangedate&order=desc&json'
    BEGIN_DATE = 19960106
    curr_list = []

    def create_curr_list(self):
        today = str(datetime.now().date()).replace('-', '')
        response = urllib.request.urlopen(self.FOR_CURR_LIST.replace('yyyymmdd', today))
        data = json.load(response)
        for el in data:
            self.curr_list.append(el['cc'])

    def check_date(self, date):
        today = str(datetime.now().date()).replace('-', '')
        date = int(date)
        if date < self.BEGIN_DATE or date > int(today):
            return False
        else:
            return True

    def date_validation(self, date):
        year = date[:4]
        month = date[4:6]
        day = date[6:]
        print(year)
        print(month)
        print(day)
        check = True
        try:
            datetime(int(year), int(month), int(day))
        except ValueError:
            check = False
        return check

    def check_code(self, code):
        if code in self.curr_list:
            return True
        else:
            return False

    def get_user_data(self, num):
        self.create_curr_list()
        print('Please enter the currency code. Please input the currency code according the list below:')
        for el in self.curr_list:
            print(f'| {el} |', end='')
        print('\n')
        currency_code = input('Please enter the currency code -> ')
        if num == 1:
            date_start = input('Please enter a date. Please use format YYYYMMDD -> ')
            date_end = date_start
        elif num == 2:
            date_start = input('Please enter a start date. Please use format YYYYMMDD -> ')
            date_end = input('Please enter an end date. Please use format YYYYMMDD -> ')
        if self.site_parse(self.prepare_url(date_start, date_end, currency_code)):
            if self.check_code(currency_code) and self.check_date(date_start) and self.check_date(date_end):
                self.print_rates(self.site_parse(self.prepare_url(date_start, date_end, currency_code)))
            else:
                print('Input error! Please enter correct data')
        else:
            print('Connection problem, try later!')

    def site_parse(self, active_url):
        response = urllib.request.urlopen(active_url)
        if response.status == 200:
            data = json.load(response)
            return data
        else:
            return None

    def print_rates(self, data):
        for el in data:
            print(f'The {el["enname"] if el["enname"] else el["cc"]} rate for the date '
                  f'{el["exchangedate"]} is {el["rate"]} UAH per {el["units"]} {el["cc"]}')

    def prepare_url(self, date_start, date_end, currency_code):
        return self.url_to_get.replace('_date_start_to_change_', date_start)\
            .replace('_date_end_to_change_', date_end).replace('_code_to_change_', currency_code)

    def workflow(self):
        active = True
        while active:
            command = self.menu()
            if command == 1:
                self.get_user_data(command)
            elif command == 2:
                self.get_user_data(command)
            elif command == 0:
                print("Session finished!")
                active = False
            else:
                print('Please enter correct menu number!')

    @staticmethod
    def menu():
        print('|| Currency rate for date: enter "1" || Currency rate for period: enter "2" || Exit: enter "0" ||')
        try:
            command = int(input('Please enter the command:'))
            return command
        except ValueError:
            print("Please enter correct menu number!")


if __name__ == '__main__':
    site = SiteRequest()
    site.workflow()






