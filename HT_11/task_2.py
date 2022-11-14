# Створити клас Person, в якому буде присутнім метод __init__ який буде приймати якісь аргументи, які зберігатиме
# в відповідні змінні.
# - Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
# - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атрибут profession (його не має інсувати
# під час ініціалізації в самому класі) та виведіть його на екран (прінтоніть)

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_age(self):
        return self.age

    def print_name(self):
        print(f'Hello, you are {self.name}!')

    def show_all_information(self):
        return [self.name, self.age]


person_1 = Person('Anna', 32)
person_2 = Person('Paul', 48)

person_1.profession = 'Dancer'
person_2.profession = 'Pilot'

person_1.print_name()
print(f'The {person_1.show_all_information()[0]} profession is {person_1.profession} and she is {person_1.age}!')
person_2.print_name()
print(f'The {person_2.show_all_information()[0]} profession is {person_2.profession} and he is {person_2.age}!')