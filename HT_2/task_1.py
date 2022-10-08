# Write a script which accepts a sequence of comma-separated numbers 
# from user and generates a list and a tuple with those numbers
#
# Version 1: a list or a tuple is with original values type of input
# string type

string_1 = input()
list_1 = (string_1.split(','))
tuple_1 = tuple(list_1)
print(f'List: {list_1} \nTuple: {tuple_1}')
