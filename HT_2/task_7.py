# Write a script to concatenate all elements in a list into a 
# string and print it. List must include both strings and 
# integers and must be hardcoded.

list_1 = [1, 2, 'u', 'a', 4, True, False]
string_1 = ''
for element in list_1:
	string_1 += str(element)
print(string_1)
