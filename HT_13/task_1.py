# 1. Створіть клас Car, який буде мати властивість year (рік випуску). Додайте всі необхідні методи до класу, щоб
# можна було виконувати порівняння car1 > car2 , яке буде показувати, що car1 старша за car2. Також, операція car1
# - car2 повинна повернути різницю між роками випуску.

from functools import total_ordering

class Car(object):

    def __init__(self, year):
        self.year = year

    def __sub__(self, other):
        return self.year - other.year

    @total_ordering
    def __eq__(self, other):
        if self.year == other.year:
            return True
        else:
            return False

    @total_ordering
    def __le__(self, other):
        if self.year >= other.year:
            return True
        else:
            return False

    @total_ordering
    def __lt__(self, other):
        if self.year > other.year:
            return True
        else:
            return False

'''
    def __gt__(self, other):
        if self.year < other.year:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.year <= other.year:
            return True
        else:
            return False
'''

car_1 = Car(1990)
car_2 = Car(1997)

print(car_1 - car_2)
print(car_1 < car_2)
print(car_1 <= car_2)
print(car_1 > car_2)
print(car_1 >= car_2)