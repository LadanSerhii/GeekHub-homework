def basel_problem(number):
	"""Sum of Euler numbers"""
	if number == 1:
		return 1
	else:
		return basel_problem(number - 1) + 1 / (number * number)

def fibonachi_numbers(number):
	"""Return Fibonachi numbers to position in arg"""
	fib_numbers = [0, 1]
	for index in range(2, number + 1):
		fib_numbers.append(fib_numbers[index-2] + fib_numbers[index-1])
	return fib_numbers

def pow_sum(lst, pow):
	"""Returns the sum on 1/(element in pow)"""
	sm = 0
	for element in lst:
		if element:
			sm += 1 / element
	return sm

def combination(number):
	lst = []
	for element in fibonachi_numbers(number):
		lst.append(element / basel_problem(number * 4) + pow_sum(fibonachi_numbers(number + 90), 12))
	return lst

print(combination(int(input('Please input a number: '))))