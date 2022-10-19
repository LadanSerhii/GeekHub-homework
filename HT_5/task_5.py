# Написати функцію <fibonacci>, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.

def fibonacci(number):
	fib_numbers = [0, 1, 1]
	number = int(number)
	index = 2
	while(fib_numbers[index] + fib_numbers[index - 1] <= number):
		fib_numbers.append(fib_numbers[index] + fib_numbers[index - 1])
		index += 1
	return fib_numbers


print(fibonacci(input("Enter the number: ")))