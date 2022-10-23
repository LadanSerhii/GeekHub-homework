# 1. Створіть функцію, всередині якої будуть записано СПИСОК із п'яти користувачів (ім'я та пароль). Функція
# повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр
# <silent> (значення за замовчуванням - <False>).
# Логіка наступна:
#     якщо введено правильну пару ім'я/пароль - вертається True;
#     якщо введено неправильну пару ім'я/пароль:
#         якщо silent == True - функція повертає False
#         якщо silent == False - породжується виключення LoginException (його також треба створити =))


class LoginException(Exception):
    pass


def user_ident(username, password, silent=False):
    user_list = [('Osborne', 'Black%12'), ('Tyler', 'Aero_04'), ('Bon Jovi', 'Johny The Rocker'), \
                 ('Ulrich', 'Vitallica'), ('Kilmister', 'Motor')]
    usr_tuple = tuple([username, password])
    try:
        if usr_tuple in user_list:
            return True
        else:
            if not silent:
                return True
            else:
                raise LoginException
    except LoginException:
        print('Custom exception raised!')


print(user_ident('Osborne', 'Black%12', True))