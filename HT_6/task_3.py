# На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
# а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції)
# - як валідні, так і ні;
# б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує
# для кожної пари значень відповідне повідомлення, наприклад:      Name: vasya
# Password: wasd
# Status: password must have at least one digit
# -----
# Name: vasya
# Password: vasyapupkin2000
# tatus: OK   P.S. Не забудьте використати блок try/except ;)


class NameException(Exception):
    ...


class PassSymbolLenException(Exception):
    pass


class NameSpaceException(Exception):
    pass


def user_validation(username, password):

    def num_in_pass(password):
        # To have an opportunity to extend required amount of numbers in password
        num_of_digits = 0
        for element in password:
            if element.isdigit():
                num_of_digits += 1
        return num_of_digits

    if len(username) < 3 or len(username) > 50:
        raise NameException

    if len(password) < 8 or not num_in_pass(password):
        raise PassSymbolLenException

    if ' ' in username:
        raise NameSpaceException


user_list = [('Oz', 'Black%12'), ('Tyler', 'Aero_04'), ('Bon Jovi', 'Johny The Rocker'),\
            ('Lars Ulrich', 'Vitallica_99'), ('Kilmister', 'Motor_Head_66')]

for element in user_list:
    print(f'Name: {element[0]}')
    print(f'Password: {element[1]}')
    try:
        user_validation(element[0], element[1])
        print('Status: OK\n')
    except NameException:
        print('Status: The len of mane should be 3..50 symbols!\n')
    except PassSymbolLenException:
        print('Status: The pass should contain at least 1 digit and be minimum 8 symbols length!\n')
    except NameSpaceException:
        print('Status: The name should not contain whitespace!\n')

