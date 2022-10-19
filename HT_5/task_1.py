# Написати функцію <square>, яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення у вигляді
# кортежа: периметр квадрата, площа квадрата та його діагональ.
import math


def square(side):
	try:
		return (4 * float(side), float(side) ** 2, float(side) * math.sqrt(2))
	except ValueError:
		print('Please enter correct data!')


print(square(input('Enter the square side: ')))