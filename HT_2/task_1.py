# Write a script which accepts a sequence of comma-separated numbers 
# from user and generates a list and a tuple with those numbers

string_1 = input('Please eneter numbers: ')
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
