# Write a script which accepts a <number>(int) from user and 
# generates dictionary in range <number> where key is <number> 
# and value is <number>*<number>

number = int(input('Please enter a number: '))
dict_square = dict()

for index in range(number):
	dict_square[index] = index * index

print(dict_square)
