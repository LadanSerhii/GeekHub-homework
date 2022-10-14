# Write a script to remove values duplicates from dictionary. 
# Feel free to hardcode your dictionary.

dict_1 = {
	'foo': 'bar', 
	'bar': 'buz', 
	'dou': 'jones', 
	'not dou': 'jones',
	'USD': 36,
	'AUD': 19.2,
	'Tamara': 19.2,
	'test_1': [1],
	'test_2': [1]
}

new_dict = dict()
values = []

for key, value in dict_1.items():
	if value not in values:
		values.append(value)
		new_dict[key] = value

dict_1 = new_dict
print(f'Updated dictionary: {dict_1}')

