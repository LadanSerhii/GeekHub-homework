import math
def check_operator(str):
	operators = ('+', '-', '*', '/', '%', '//')
	if str in operators:
		return True
	else:
		return False

def check_number(str):
	try:
		float(str)
		return True
	except:
		TypeError
		return False

def check_int(number):
	if not float(number) % 1:
		return (math.floor(float(number)))
	else:
		return float(number)

def calc(x, y, operator):
	if check_number(x) and check_number(y) and check_operator(operator):
		x = check_int(x)
		y = check_int(y)
		if operator == '+':
			return check_int(x + y)
		elif operator == '-':
			return check_int(x - y)
		elif operator == '*':
			return check_int(x * y)
		elif operator == '/':
			if y:
				return check_int(x / y)
			else:
				return "Error input, you can not divide by zero"
		elif operator == '%':
			if y:
				return check_int(x % y)
			else:
				return "Error input, you can not divide by zero"
		elif operator == '//':
			if y:
				return check_int(x // y)
			else:
				return "Error input, you can not divide by zero"
	else:
		return "Error input"

x = input('Please enter X: ')
operator = input('Please enter operator: ')
y = input('Please enter Y: ')
print(calc(x, y, operator))