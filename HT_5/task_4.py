# Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець діапазона, і
# вертатиме список простих чисел всередині цього діапазона. Не забудьте про перевірку на валідність
# введених даних та у випадку невідповідності - виведіть повідомлення.

def is_prime(number):
	number = int(number)
	indicator = True
	for num in range(2, number):
		if number % num == 0:
			indicator = False
			break
		else:
			continue
	return indicator


def prime_list(number_1, number_2):
	lst = []
	for element in range(number_1, number_2 + 1):
		if is_prime(element):
			lst.append(element)
	return lst


num_1 = (input('Please enetr 1st number: '))
num_2 = (input('Please enetr 2nd number: '))

try:
	num_1 = int(num_1)
	num_2 = int(num_2)
	print(prime_list(num_1, num_2))
except ValueError:
	print('Incorrect data!')


