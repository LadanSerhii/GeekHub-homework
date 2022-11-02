# Програма-банкомат.
#    Використовуючи функції створити програму з наступним функціоналом:
#       - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.CSV>);
#       - кожен з користувачів має свій поточний баланс (файл <{username}_balance.TXT>) та історію транзакцій
#       (файл <{username_transactions.JSON>);
#       - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено цифри;
#       знімається не більше, ніж є на рахунку і т.д.).
#    Особливості реалізації:
#       - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
#       - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
#       - файл з користувачами: тільки читається. Але якщо захочете реалізувати функціонал додавання нового
#       користувача - не стримуйте себе :)
#    Особливості функціонала:
#       - за кожен функціонал відповідає окрема функція;
#       - основна функція - <start()> - буде в собі містити весь workflow банкомата:
#       - на початку роботи - логін користувача (програма запитує ім'я/пароль). Якщо вони неправильні - вивести
#       повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все
#       на ентузіазмі :))
#       - потім - елементарне меню типу:
#         Введіть дію:
#            1. Подивитись баланс
#            2. Поповнити баланс
#            3. Вихід
#       - далі - фантазія і креатив, можете розширювати функціонал, але основне завдання має бути
#       повністю реалізоване :)
#     P.S. Увага! Файли мають бути саме вказаних форматів (csv, txt, json відповідно)
#     P.S.S. Добре продумайте структуру програми та функцій


import json
import csv
from datetime import datetime


def check_pass(username, password):
    with open('users.CSV') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                return True
    return False


def check_balance(username):
    filename = username + '_balance.TXT'
    with open(filename, 'r') as file:
        balance = int(file.read())
        return balance


def withdraw_balance(username, change_amount):
    filename = username + '_balance.TXT'
    with open(filename, 'r') as file:
        balance = int(file.read())
    if change_amount < 0:
        print("You could not withdraw negative value!")
    elif change_amount <= balance:
        with open(filename, 'w') as file:
            file.write(str(balance - change_amount))
        transaction(username, change_amount)
        print(f'Please take your ${change_amount} from the bin!')
    else:
        print("You have not enough of money!")


def add_balance(username, change_amount):
    filename = username + '_balance.TXT'
    with open(filename, 'r') as file:
        balance = int(file.read())
    if change_amount < 0:
        print("You could not add negative value!")
    else:
        with open(filename, 'w') as file:
            file.write(str(balance + change_amount))
        transaction(username, change_amount)
        print(f'The ${change_amount} successfully added to your account!')


def transaction(username, amount):
    filename = username + '_transactions.JSON'
    tm = datetime.now()
    with open(filename, 'r') as file:
        data = json.load(file)
    with open(filename, 'w') as file:
        data[str(tm)] = amount
        json.dump(data, file)


def print_transactions(username):
    filename = username + '_transactions.JSON'
    with open(filename, 'r') as file:
        data = json.load(file)
        print(f'Transaction history by date for {username}:')
        for row in data:
            print(f'{row} -> {data[row]}')


def menu():
    print('|| Check balance: enter "1" || Add money: enter "2" || Withdraw money: enter "3" || '
          'Check transaction history: enter "4" || Exit: enter "0" ||')
    try:
        command = int(input('Please enter the command:'))
        return command
    except ValueError:
        print("Please enter correct menu number!")


def workflow(username):
    active = True
    while(active):
        command = menu()
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
                withdraw_balance(username, change_amount)
        elif command == 4:
            print_transactions(username)
        elif command == 0:
            print("Session finished!")
            active = False
        else:
            print('Please enter correct menu number!')


def start():
    username = input('Please enter username: ')
    password = input('Please enter password: ')
    if check_pass(username, password):
        workflow(username)
    else:
        print("Wrong username and/or password!")


start()
