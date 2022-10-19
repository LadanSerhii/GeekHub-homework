# Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме True, якщо це
# число просте і False - якщо ні.


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


print(is_prime(input('Please enter a number: ')))
