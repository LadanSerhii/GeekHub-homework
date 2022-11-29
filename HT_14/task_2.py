# 2. Створіть програму для отримання курсу валют за певний період.
# - отримати від користувача дату (це може бути як один день так і інтервал - початкова і кінцева дати, продумайте
# механізм реалізації) і назву валюти
# - вивести курс по відношенню до гривні на момент вказаної дати (або за кожен день у вказаному інтервалі)
# - не забудьте перевірку на валідність введених даних

import requests
from requests.exceptions import HTTPError
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
        if self.check_response(self.FOR_CURR_LIST.replace('yyyymmdd', today)):
            response = requests.get(self.FOR_CURR_LIST.replace('yyyymmdd', today))
            data = response.json()
            for el in data:
                self.curr_list.append(el['cc'])
            return True
        else:
            return False

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
        if self.create_curr_list():
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
            data = self.site_parse(self.prepare_url(date_start, date_end, currency_code))
            if data:
                if self.check_code(currency_code) and self.check_date(date_start) and self.check_date(date_end):
                    self.print_rates(data)
                else:
                    print('Input error! Please enter correct data')
            else:
                print(f'A problem has been occurred! The status code is '
                    f'{self.response_code(prepare_url(date_start, date_end, currency_code))}. Please check it!')

    def site_parse(self, active_url):
        if self.check_response(active_url):
            response = requests.get(active_url)
            data = response.json()
            return data
        else:
            return False

    def check_response(self, active_url):
        # print('=== Checking response! ===')
        try:
            response = requests.get(active_url)
            response.raise_for_status()
        except HTTPError as http_error:
            print('==========================================    ERROR   ===========================================')
            print(f'HTTP error occurred: {http_error}')
            print('==========================================    *****   ===========================================')
            return False
        except Exception as error:
            print('==========================================    ERROR   ===========================================')
            print(f'Not HTTP error occurred: {error}. \nPlease check how to repair it!')
            print('==========================================    *****   ===========================================')

            return False
        else:
            # print(f'Successful response!')
            return True

    def responce_code(self, active_url):
        return requests.get(active_url)

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
        print('===========================================    MENU   ===========================================')
        print('|| Currency rate for date: enter "1" || Currency rate for period: enter "2" || Exit: enter "0" ||')
        print('===========================================    ****   ===========================================')
        try:
            command = int(input('Please enter the command:'))
            return command
        except ValueError:
            print("Please enter correct menu number!")


if __name__ == '__main__':
    site = SiteRequest()
    site.workflow()






