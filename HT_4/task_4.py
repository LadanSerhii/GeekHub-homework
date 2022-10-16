def action_str(string):
	num_sum = 0
	new_str = ''
	if len(string) < 30:
		for element in string:
			if element.isnumeric():
				num_sum += int(element)
			elif element.isalpha():
				new_str += element
		print(f'Sum of numbers: {num_sum}')	
		print(f'Only characters: {new_str}')	
	elif len(string) in range(30, 51):
		num_count = 0
		char_count = 0
		for element in string:
			if element.isnumeric():
				num_count += 1
			elif element.isalpha():
				char_count += 1	
		print(f'Length: {len(string)}, numbers: {num_count},\
characters: {char_count}')
	elif len(string) > 50:
		lst = []	
		for element in string:
			if element.isalnum():
				lst.append(element)
		print(lst)

action_str(input('Please type a string: '))
