# 1. Додайте до банкомату меню отримання поточного курсу валют за допомогою requests
# (можна використати відкрите API ПриватБанку)


import sqlite3
from datetime import datetime
import random
import requests


class NameException(Exception):
    pass


class PassSymbolLenException(Exception):
    pass


def num_in_pass(password):
    num_of_digits = 0
    for element in password:
        if element.isdigit():
            num_of_digits += 1
    return num_of_digits


class User(object):
    """The class to create the active user during session with ATM.

    The class has some internal functions to interact with ATM database.
    As an option for a future the parameter "password" could be deleted
    in future for data protection and easiest working code working.

    """

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_balance(self):
        """Function to add money to the customer's balance, work with the table of users"""
        username = self.username
        conn = sqlite3.connect('atm.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT BALANCE FROM USERS WHERE NAME=?''', (username,))
        data = cursor.fetchone()
        return data[0]

    def withdraw_balance(self, change_amount):
        conn = sqlite3.connect('atm.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ATMBALANCE")
        atm_data = cursor.fetchall()
        atm_balance = 0
        for row in atm_data:
            atm_balance += row[0] * row[1]
        cursor.execute('''SELECT BALANCE FROM USERS WHERE NAME=?''', (self.username,))
        data = cursor.fetchone()
        balance = data[0]
        if change_amount < 0:
            print("You could not withdraw negative value!")
        elif change_amount > atm_balance:
            print("Not enough money in ATM!")
        elif change_amount > balance:
            print("You have not enough of money on your account!")
        else:
            self.withdraw(change_amount)

    def withdraw(self, amount):
        conn = sqlite3.connect('atm.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT NOMINAL, QUANTITY FROM ATMBALANCE''')
        atm_bal = cursor.fetchall()
        # atm_bal = [(10, 5), (20, 1), (50, 1), (100, 0), (200, 4), (500, 1), (1000, 5)]
        delta = amount
        banknote_list = []
        for el in atm_bal:
            for index in range(el[1]):
                banknote_list.append(el[0])
        banknote_list.reverse()
        banknote_list.sort()
        pos_amount = [(0, 0)]
        for elem in banknote_list:
            tmp_pos_amount = []
            for el in pos_amount:
                tmp = (el[0] + elem, elem)
                tmp_pos_amount.append(tmp)
            for el in tmp_pos_amount:
                if el[0] <= amount and el not in pos_amount:
                    pos_amount.append(el)
            pos_amount.sort()
            pos_amount.reverse()
        if self.possibility_of_withdraw(amount, pos_amount):
            combination = []
            while amount != 0:
                for el in pos_amount:
                    if el[0] == amount:
                        combination.append(el[1])
                        amount -= el[1]
            combination_dict = {}
            for el in combination:
                if el != 0:
                    if el not in combination_dict.keys():
                        combination_dict[el] = combination.count(el)
            atm_bal_dict = {}
            for el in atm_bal:
                atm_bal_dict[el[0]] = el[1]
            print(f'Please take your:')
            for key in combination_dict:
                if combination_dict[key] != 0:
                    print(f'{combination_dict[key]} * ${key}')
                    cursor.execute('''UPDATE ATMBALANCE SET QUANTITY=? WHERE NOMINAL=?''',
                                   (atm_bal_dict[key] - combination_dict[key], key,))
                    cursor.execute('''SELECT BALANCE FROM USERS WHERE NAME=?''', (self.username,))
                    balance = cursor.fetchone()
                    cursor.execute('''UPDATE USERS SET BALANCE=? WHERE NAME=?''',
                                   (balance[0] - delta, self.username,))
                    conn.commit()
                    self.transaction(-delta)
        else:
            print(f'The amount could not be given with the existing nominals!')

    def add_balance(self, change_amount):
        conn = sqlite3.connect('atm.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT NOMINAL FROM ATMBALANCE''')
        data = cursor.fetchall()
        nominals = []
        for element in data:
            nominals.append(element[0])
        cursor.execute('''SELECT BALANCE FROM USERS WHERE NAME=?''', (self.username,))
        data = cursor.fetchone()
        balance = data[0]
        if change_amount < 0:
            print("You could not add negative value!")
        else:
            if not change_amount % min(nominals):
                cursor.execute('''UPDATE USERS SET BALANCE=? WHERE NAME=?''', (balance + change_amount, self.username,))
                conn.commit()
                self.transaction(change_amount)
                print(f'The ${change_amount} successfully added to your account!')
            else:
                difference = change_amount % min(nominals)
                change_amount = change_amount - difference

                print(change_amount)
                cursor.execute('''UPDATE USERS SET BALANCE=? WHERE NAME=?''', (balance + change_amount, self.username,))
                conn.commit()
                self.transaction(change_amount)
                print(f'The ${change_amount} successfully added to your account!')
                print(f'Please take the ${difference} back!')
        conn.close()

    def transaction(self, amount):
        conn = sqlite3.connect('atm.db')
        cursor = conn.cursor()
        tm = datetime.now()
        cursor.execute('''INSERT INTO TRANSACTIONS (NAME, TIME, BALANCE) VALUES(?, ?, ?)''',
                       (self.username, tm, amount))
        conn.commit()
        conn.close()

    def print_transactions(self):
        conn = sqlite3.connect('atm.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM TRANSACTIONS WHERE NAME=?''', (self.username,))
        data = cursor
        for row in data:
            print(f'{row[2]} -> {row[3]}')

    @staticmethod
    def possibility_of_withdraw(amount, pos_amount):
            amount_list = []
            for el in pos_amount:
                amount_list.append(el[0])
            if amount in amount_list:
                return True
            else:
                return False

    @staticmethod
    def print_currency_rate():
        try:
            response_API = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11')
            if response_API.status_code == 200:
                data = response_API.json()
                for ccy in data:
                    print(f'The {ccy.get("ccy")} rate is: Buy -> {ccy.get("buy")}, Sale -> {ccy.get("sale")}')
            else:
                print('Connection problem, please try to check later!')
        except Exception:
            print('Connection problem, please try to check later!')


class Service(object):
    def __init__(self, username):
        self.username = username

    def atm_add(self):
        banknote_nominal = int(input('Please enter the nominal of banknotes: '))
        banknote_amount = int(input('Please enter the amount of banknotes (plus/minus for add/grab): '))
        conn = sqlite3.connect('atm.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT NOMINAL FROM ATMBALANCE''')
        data = cursor.fetchall()
        nominals = []
        cursor.execute('''SELECT QUANTITY FROM ATMBALANCE WHERE NOMINAL=?''', (banknote_nominal,))
        amount = cursor.fetchone()
        for element in data:
            nominals.append(element[0])
        if banknote_nominal not in nominals:
            print('Wrong nominal input!')
        elif -amount[0] > banknote_amount:
            print(f'Not enough of banknotes ${banknote_nominal} to grab!')
        else:
            self.transaction(banknote_nominal * banknote_amount)
            banknote_amount += amount[0]
            cursor.execute('''UPDATE ATMBALANCE SET QUANTITY=? WHERE NOMINAL=?''', (banknote_amount, banknote_nominal,))
            conn.commit()

        conn.close()

    @staticmethod
    def atm_balance_print():
        conn = sqlite3.connect('atm.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ATMBALANCE")
        atm_data = cursor.fetchall()
        atm_balance = 0
        for row in atm_data:
            atm_balance += row[0] * row[1]
        print(f'ATM alance is: ${atm_balance}')
        for row in atm_data:
            print(f'${row[0]} -> {row[1]} banknotes left!')

    @staticmethod
    def print_transactions_all():
        conn = sqlite3.connect('atm.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM TRANSACTIONS''')
        data = cursor
        for row in data:
            print(f'{row[1]}  {row[2]} -> {row[3]}')

    def print_transactions(self):
        conn = sqlite3.connect('atm.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM TRANSACTIONS WHERE NAME=?''', (self.username,))
        data = cursor
        for row in data:
            print(f'{row[2]} -> {row[3]}')

    def transaction(self, amount):
        conn = sqlite3.connect('atm.db')
        cursor = conn.cursor()
        tm = datetime.now()
        cursor.execute('''INSERT INTO TRANSACTIONS (NAME, TIME, BALANCE) VALUES(?, ?, ?)''',
                       (self.username, tm, amount))
        conn.commit()
        conn.close()


def user_validation(username, password):
    if len(username) < 3 or len(username) > 50:
        raise NameException('The len of mane should be 3..50 symbols!')
    if len(password) < 8 or not num_in_pass(password):
        raise PassSymbolLenException('The pass should contain at least 1 digit and be minimum 8 symbols length')


def create_user():
    username = input('Please enter the username:')
    password = input('Please enter the password:')
    try:
        user_validation(username, password)
        conn = sqlite3.connect('atm.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT NAME FROM USERS''')
        names = cursor.fetchall()
        name_list = []
        for name in names:
            name_list.append(name[0])
        if username not in name_list:
            cursor.execute('''INSERT INTO USERS (NAME, PASSWORD, BALANCE, SERVICE) VALUES(?, ?, ?, ?)''',
                            (username, password, 0, 'FALSE'))
            conn.commit()
            number = int(input(f'You have an opportunity of 10% to get the BONUS! Please enter a number from 0 to 9: '))
            rnd = random.randint(0, 9)
            if number == rnd:
                print(f'Match! {number} is equal to {rnd}!You have a bonus of $1000 on your account!')
                active_user = User(username, password)
                active_user.add_balance(1000)
                print(f'The username "{username}" created!')
                user_workflow(active_user)
            else:
                print(f'Sorry, {number} is not equal to {rnd}! You have no bonus!')
                active_user = User(username, password)
                print(f'The username "{username}" created!')
                user_workflow(active_user)
        else:
            print(f'The username "{username}" is already exist!')
        conn.close()
    except NameException as e:
        print(e)
    except PassSymbolLenException as e:
        print(e)


def get_password(username):
    conn = sqlite3.connect('atm.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM USERS WHERE NAME=?''', (username,))
    data = cursor.fetchone()
    try:
        return [data[2], data[4]]
    except Exception:
        return False


def check_pass(username, password):
    user_pass = get_password(username)
    if user_pass:
        if user_pass[0] == password and user_pass[1] != "TRUE":
            return True
        elif user_pass[0] == password and user_pass[1] == "TRUE":
            print('Please login in service mode!')
            return False
    else:
        return False


def check_service(username, password):
    user_pass = get_password(username)
    if user_pass:
        if user_pass[0] == password and user_pass[1] == "TRUE":
            return True
        elif user_pass[0] == password and user_pass[1] != "TRUE":
            print('You have not service permissions!')
            return False
    else:
        return False


def workflow():
    active = True
    while active:
        command = menu()
        if command == 1:
            start_user()
        elif command == 2:
            create_user()
        elif command == 3:
            start_service()
        elif command == 0:
            print("Session finished!")
            active = False
        else:
            print('Please enter correct menu number!')


def start_user():
    username = input('Please enter username: ')
    password = input('Please enter password: ')
    if check_pass(username, password):
        active_user = User(username, password)
        user_workflow(active_user)
    else:
        print("Wrong username and/or password!")


def start_service():
    username = input('Please enter username: ')
    password = input('Please enter password: ')
    if check_service(username, password):
        active_service = Service(username)
        service_workflow(active_service)
    else:
        print("Wrong username and/or password!")


def user_workflow(active_user):
    active = True
    while active:
        command = user_menu()
        if command == 1:
            print(f'Dear {active_user.username}, you have ${active_user.check_balance()} on your account!')
        elif command == 2:
            amount = input('Please enter the amount of money to add:')
            try:
                change_amount = int(amount)
                active_user.add_balance(change_amount)
            except ValueError:
                print('Wrong value entered!')
        elif command == 3:
            amount = input('Please enter the amount of money to withdraw:')
            try:
                change_amount = int(amount)
                active_user.withdraw_balance(change_amount)
            except ValueError:
                print('Wrong value entered!')
        elif command == 4:
            active_user.print_transactions()
        elif command == 5:
            active_user.print_currency_rate()
        elif command == 0:
            print("Session finished!")
            active = False
        else:
            print('Please enter correct menu number!')


def service_workflow(active_service):
    active = True
    while active:
        command = service_menu()
        if command == 1:
            active_service.atm_balance_print()
        elif command == 2:
            active_service.atm_add()
        elif command == 3:
            active_service.print_transactions()
        elif command == 4:
            active_service.print_transactions_all()
        elif command == 0:
            print("Session finished!")
            active = False
        else:
            print('Please enter correct menu number!')


def menu():
    print('|| Login: enter "1" || Create new user: enter "2" || Service mode: enter "3" || Exit: enter "0" ||')
    try:
        command = int(input('Please enter the command:'))
        return command
    except ValueError:
        print("Please enter correct menu number!")


def user_menu():
    print('|| Check balance: enter "1" || Add money: enter "2" || Withdraw money: enter "3" || '
          'Check transaction history: enter "4" || Check actual currency rates: enter "5" || Exit: enter "0" ||')
    try:
        command = int(input('Please enter the command:'))
        return command
    except ValueError:
        print("Please enter correct menu number!")


def service_menu():
    print('|| Check ATM balance: enter "1" || Change ATM balance: enter "2" || '
          'Check transaction history: enter "3" || Browse all transactions: enter "4" || Exit: enter "0" ||')
    try:
        command = int(input('Please enter the command:'))
        return command
    except ValueError:
        print("Please enter correct menu number!")


def start():
    workflow()


def atm_balance(atm_bal):
    nominals = []
    for nominal in atm_bal.keys():
        nominals.append(nominal)
    balance = 0
    for nominal in nominals:
        balance += nominal * atm_bal[nominal]
    return balance


def atm_nominals(atm_bal):
    nominals = []
    for nominal in atm_bal.keys():
        nominals.append(nominal)
    return nominals


start()