# Write a script to concatenate the following dictionaries to 
# create a NEW one.
# dict_1 = {'foo': 'bar', 'bar': 'buz'}
# dict_2 = {'dou': 'jones', 'USD': 36}
# dict_3 = {'AUD': 19.2, 'name': 'Tom'}

dict_1 = {'foo': 'bar', 'bar': 'buz'}
dict_2 = {'dou': 'jones', 'USD': 36}
dict_3 = {'AUD': 19.2, 'name': 'Tom'}

dict_list = [dict_1, dict_2, dict_3]
new_dict = dict()

for el in dict_list:
	new_dict.update(el)
print(new_dict)
