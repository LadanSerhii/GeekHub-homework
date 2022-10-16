def num_compare(x, y):
	if x > y:
		return f'{x} бiльше нiж {y} на {x-y}'
	elif x < y:
		return f'{y} бiльше нiж {x} на {y-x}'
	elif x == y:
		return f'{x} дорівнює {y}'

x, y = input('Please enter X and Y: ').split()
print((num_compare(int(x), int(y))))