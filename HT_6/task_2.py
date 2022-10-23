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

    if ' ' in username:
        raise NameSpaceException('The name should not contain whitespace!')