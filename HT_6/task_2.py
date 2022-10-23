# Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#    - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#    - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
#    цифру;
#    - якесь власне додаткове правило :)
#    Якщо якийсь із параметрів не відповідає вимогам - породити виключення із відповідним текстом.


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


try:
    user_validation('Ozfdrdd', 'A')
except NameException:
    print('NameException')
except PassSymbolLenException:
    print('PassSymbolLenException')
except NameSpaceException:
    print('NameSpaceException')