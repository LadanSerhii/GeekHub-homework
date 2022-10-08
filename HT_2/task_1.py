# Write a script which accepts a sequence of comma-separated numbers 
# from user and generates a list and a tuple with those numbers
#
# Version 2: as listed in the statement the values are numbers, so
# list or a tuple is with number (integer in this case) values


string_1 = input()
list_1 = (string_1.split(','))
for i in range(len(list_1)):
	if list_1[i].isnumeric():
		list_1[i] = int(list_1[i])
	else:
		print('Input value error!')
		break
tuple_1 = tuple(list_1)
a = list_1[0]
print(type(a))
print(f'List: {list_1} \nTuple: {tuple_1}')
