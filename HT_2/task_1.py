# Write a script which accepts a sequence of comma-separated numbers 
# from user and generates a list and a tuple with those numbers

string_1 = input()
list_1 = (string_1.split(','))
tuple_1 = tuple(list_1)
print(f'List: {list_1} \nTuple: {tuple_1}')

a = list_1[0]
print(type(a))
