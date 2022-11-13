# Банкомат 3.0
# - реалізуйте видачу купюр за логікою видавання найменшої кількості купюр, але в межах наявних в банкоматі. Наприклад:
# 2560 --> 2х1000, 1х500, 3х20. Будьте обережні з "жадібним алгоритмом"! Видані купюри також мають бути “вилучені”
# з банкомату. Тобто якщо до операції в банкоматі було 5х1000, 5х500, 5х20 - має стати 3х1000, 4х500, 2х20.
# - як і раніше, поповнення балансу користувача не впливає на кількість купюр. Їх кількість може змінювати лише
# інкасатор.
# - обов’язкова реалізація таких дій (назви можете використовувати свої):
# При запускі
# Вхід
# Реєстрація (з перевіркою валідності/складності введених даних)
# Вихід
# Для користувача
# Баланс
# Поповнення
# Зняття
# Історія транзакцій
# Вихід на стартове меню
# Для інкасатора
# Наявні купюри/баланс тощо
# Зміна кількості купюр
# Повна історія операцій по банкомату (дії всіх користувачів та інкасаторів)
# Вихід на стартове меню
# - обов’язкове дотримання РЕР8 (якщо самостійно ніяк, то https://flake8.pycqa.org/en/latest/ вам в допомогу)
# - (опціонально) не лініться і придумайте якусь свою особливу фішку/додатковий функціонал, але при умові що
# основне завдання виконане


import sqlite3
from datetime import datetime


class NameException(Exception):
    pass


class PassSymbolLenException(Exception):
    pass


def num_in_pass(password):
# To have an opportunity to extend required amount of numbers in password
    num_of_digits = 0
    for element in password:
        if element.isdigit():
            num_of_digits += 1
    return num_of_digits


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
            print(f'The username "{username}" created!')
            user_workflow(username)
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
    cursor.execute('''SELECT * FROM USERS WHERE NAME=?''', (username, ))
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


def check_balance(username):
    conn = sqlite3.connect('atm.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT BALANCE FROM USERS WHERE NAME=?''', (username, ))
    data = cursor.fetchone()
    return data[0]


def withdraw_balance(username, change_amount):
    conn = sqlite3.connect('atm.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ATMBALANCE")
    atm_data = cursor.fetchall()
    atm_balance = 0
    for row in atm_data:
        atm_balance += row[0] * row[1]
    cursor.execute('''SELECT BALANCE FROM USERS WHERE NAME=?''', (username, ))
    data = cursor.fetchone()
    balance = data[0]
    if change_amount < 0:
        print("You could not withdraw negative value!")
    elif change_amount > atm_balance:
        print("Not enough money in ATM!")
    elif change_amount > balance:
        print("You have not enough of money on your account!")
    else:
        withdraw(username, change_amount)


def add_balance(username, change_amount):
    conn = sqlite3.connect('atm.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT NOMINAL FROM ATMBALANCE''')
    data = cursor.fetchall()
    nominals = []
    for element in data:
        nominals.append(element[0])
    cursor.execute('''SELECT BALANCE FROM USERS WHERE NAME=?''', (username, ))
    data = cursor.fetchone()
    balance = data[0]
    if change_amount < 0:
        print("You could not add negative value!")
    else:
        if not change_amount % min(nominals):
            cursor.execute('''UPDATE USERS SET BALANCE=? WHERE NAME=?''', (balance + change_amount, username,))
            conn.commit()
            transaction(username, change_amount)
            print(f'The ${change_amount} successfully added to your account!')
        else:
            difference = change_amount % min(nominals)
            change_amount = change_amount - difference

            print(change_amount)
            cursor.execute('''UPDATE USERS SET BALANCE=? WHERE NAME=?''', (balance + change_amount, username,))
            conn.commit()
            transaction(username, change_amount)
            print(f'The ${change_amount} successfully added to your account!')
            print(f'Please take the ${difference} back!')

    conn.close()


def transaction(username, amount):
    conn = sqlite3.connect('atm.db')
    cursor = conn.cursor()
    tm = datetime.now()
    cursor.execute('''INSERT INTO TRANSACTIONS (NAME, TIME, BALANCE) VALUES(?, ?, ?)''',
                   (username, tm, amount))
    conn.commit()
    conn.close()


def print_transactions(username):
    conn = sqlite3.connect('atm.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM TRANSACTIONS WHERE NAME=?''', (username, ))
    data = cursor
    for row in data:
        print(f'{row[2]} -> {row[3]}')


def print_transactions_all():
    conn = sqlite3.connect('atm.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM TRANSACTIONS''')
    data = cursor
    for row in data:
        print(f'{row[1]}  {row[2]} -> {row[3]}')


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


def user_workflow(username):
    active = True
    while active:
        command = user_menu()
        if command == 1:
            print(f'Dear {username}, you have ${check_balance(username)} on your account!')
        elif command == 2:
            amount = input('Please enter the amount of money to add:')
            try:
                change_amount = int(amount)
                add_balance(username, change_amount)
            except ValueError:
                print('Wrong value entered!')
        elif command == 3:
            amount = input('Please enter the amount of money to withdraw:')
            try:
                change_amount = int(amount)
                withdraw_balance(username, change_amount)
            except ValueError:
                print('Wrong value entered!')
        elif command == 4:
            print_transactions(username)
        elif command == 0:
            print("Session finished!")
            active = False
        else:
            print('Please enter correct menu number!')


def service_workflow(username):
    active = True
    while active:
        command = service_menu()
        if command == 1:
            atm_balance_print()
        elif command == 2:
            atm_add(username)
        elif command == 3:
            print_transactions(username)
        elif command == 4:
            print_transactions_all()
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
          'Check transaction history: enter "4" || Exit: enter "0" ||')
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


def start_user():
    username = input('Please enter username: ')
    password = input('Please enter password: ')
    if check_pass(username, password):
        user_workflow(username)
    else:
        print("Wrong username and/or password!")


def start_service():
    username = input('Please enter username: ')
    password = input('Please enter password: ')
    if check_service(username, password):
        service_workflow(username)
    else:
        print("Wrong username and/or password!")


def start():
    workflow()


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


def atm_add(username):
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
        transaction(username, banknote_nominal * banknote_amount)
        banknote_amount += amount[0]
        cursor.execute('''UPDATE ATMBALANCE SET QUANTITY=? WHERE NOMINAL=?''', (banknote_amount, banknote_nominal, ))
        conn.commit()

    conn.close()


def reduce_nominals(amount, nominals):
    while amount < max(nominals):
        nominals.pop()
    return nominals


def reduce_nominals_second(amount, nominals):
    while amount < max(nominals):
        nominals.pop()
    nominals.pop()
    return nominals


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


def possibility_of_withdraw(amount, pos_amount):
    amount_list = []
    for el in pos_amount:
        amount_list.append(el[0])
    if amount in amount_list:
        return True
    else:
        return False


def withdraw(username, amount):
    conn = sqlite3.connect('atm.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT NOMINAL, QUANTITY FROM ATMBALANCE''')
    atm_bal = cursor.fetchall()
    #atm_bal = [(10, 5), (20, 1), (50, 1), (100, 0), (200, 4), (500, 1), (1000, 5)]
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
    if possibility_of_withdraw(amount, pos_amount):
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
                cursor.execute('''SELECT BALANCE FROM USERS WHERE NAME=?''', (username, ))
                balance = cursor.fetchone()
                cursor.execute('''UPDATE USERS SET BALANCE=? WHERE NAME=?''',
                               (balance[0] - delta, username,))
                conn.commit()
                transaction(username, delta)
    else:
        print(f'The amount could not be given with the existing nominals!')


start()