# Write a script that will run through a list of tuples and replace 
# the last value for each tuple. The list of tuples can be hardcoded. 
# The "replacement" value is entered by user. The number of elements 
# in the tuples must be different.


list_of_tuples = [('The Trooper', 4, 'test', 2.5, [1, 4, 8]), ([1, 1, 1]), 
	('value x', 'value y', 17, 'crazy train'), ()]
rep_value = input('Enter the value to change on last pos. in tuple: ')

for index in range(len(list_of_tuples)):
	temp_list = list(list_of_tuples[index])
	if temp_list:
		temp_list.pop()
		temp_list.append(rep_value)
		list_of_tuples[index] = tuple(temp_list)

print(list_of_tuples)
