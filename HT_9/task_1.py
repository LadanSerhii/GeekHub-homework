# Банкомат 2.0
#     - усі дані зберігаються тільки в sqlite3 базі даних у відповідних таблицях. Більше ніяких файлів. Якщо в
#     попередньому завданні ви добре продумали структуру програми то у вас не виникне проблем швидко адаптувати її
#     до нових вимог.
#     - на старті додати можливість залогінитися або створити нового користувача (при створенні нового користувача,
#     перевіряється відповідність логіну і паролю мінімальним вимогам. Для перевірки створіть окремі функції)
#     - в таблиці з користувачами також має бути створений унікальний користувач-інкасатор, який матиме розширені
#     можливості (домовимось, що логін/пароль будуть admin/admin щоб нам було простіше перевіряти)
#     - банкомат має власний баланс
#     - кількість купюр в банкоматі обмежена (тобто має зберігатися номінал та кількість). Номінали купюр -
#     10, 20, 50, 100, 200, 500, 1000
#     - змінювати вручну кількість купюр або подивитися їх залишок в банкоматі може лише інкасатор
#     - користувач через банкомат може покласти на рахунок лише суму кратну мінімальному номіналу що підтримує
#     банкомат. В іншому випадку - повернути "здачу" (наприклад при поклажі 1005 --> повернути 5). Але це не має
#     впливати на баланс/кількість купюр банкомату, лише збільшується баланс користувача (моделюємо наявність двох
#     незалежних касет в банкоматі - одна на прийом, інша на видачу)
#     - зняти можна лише в межах власного балансу, але не більше ніж є всього в банкоматі.
#     - при неможливості виконання якоїсь операції - вивести повідомлення з причиною (невірний логін/пароль,
#     недостатньо коштів на рахунку, неможливо видати суму наявними купюрами тощо.)
#     - файл бази даних з усіма створеними таблицями і даними також додайте в репозиторій, що б ми могли його
#     використати


import sqlite3
from datetime import datetime


class NameException(Exception):
    ...


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
    if get_password(username):
        if get_password(username)[0] == password and get_password(username)[1] != "TRUE":
            return True
        elif get_password(username)[0] == password and get_password(username)[1] == "TRUE":
            print('Please login in service mode!')
            return False
    else:
        return False


def check_service(username, password):
    if get_password(username):
        if get_password(username)[0] == password and get_password(username)[1] == "TRUE":
            return True
        elif get_password(username)[0] == password and get_password(username)[1] != "TRUE":
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
        cursor.execute('''UPDATE USERS SET BALANCE=? WHERE NAME=?''', (balance - change_amount, username, ))
        conn.commit()
        transaction(username, -change_amount)
        print(f'Please take your ${change_amount} from the bin!')
    conn.close()


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


def service_workflow():
    active = True
    while active:
        command = service_menu()
        if command == 1:
            atm_balance()
        elif command == 2:
            atm_add()
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
    print('|| Check ATM balance: enter "1" || Change ATM balance: enter "2" || Exit: enter "0" ||')
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
        service_workflow()
    else:
        print("Wrong username and/or password!")


def start():
    workflow()


def atm_balance():
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


def atm_add():
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
        banknote_amount += amount[0]
        cursor.execute('''UPDATE ATMBALANCE SET QUANTITY=? WHERE NOMINAL=?''', (banknote_amount, banknote_nominal, ))
        conn.commit()
    conn.close()


start()

