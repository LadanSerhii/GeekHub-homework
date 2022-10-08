# Write a script to check whether a value from user input is 
# contained in a group of values.
# e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
#      [1, 2, 'u', 'a', 4, True] --> 5 --> False

st = input()
list_1 = [1, 2, 'u', 'a', 4, True]
for index in range(len(list_1)):
	list_1[index] = str(list_1[index])
print(st in list_1)

