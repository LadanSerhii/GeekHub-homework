# Write a script to check whether a value from user input is 
# contained in a group of values.
# e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
#      [1, 2, 'u', 'a', 4, True] --> 5 --> False

st = input('Please enter a value to check: ')
list_1 = [1, 2, 'u', 'a', 4, True]

for item in list_1:
	list_1[list_1.index(item)] = str(item)
print(f'The result of checking value in list: {st in list_1}')
