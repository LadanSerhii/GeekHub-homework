# Write a script to remove values duplicates from dictionary. 
# Feel free to hardcode your dictionary.

dict_1 = {
	'foo': 'bar', 
	'bar': 'buz', 
	'dou': 'jones', 
	'not dou': 'jones',
	'USD': 36,
	'AUD': 19.2,
	'Tamara': 19.2
}

for item in dict_1.copy():
	tmp_dict = dict_1.copy()
	tmp_dict.pop(item)
	if set(dict_1.values()) == set(tmp_dict.values()):
		dict_1.pop(item)

print(f'Updated dictionary: {dict_1}')

