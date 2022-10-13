# Write a script to concatenate the following dictionaries to 
# create a NEW one.
# dict_1 = {'foo': 'bar', 'bar': 'buz'}
# dict_2 = {'dou': 'jones', 'USD': 36}
# dict_3 = {'AUD': 19.2, 'name': 'Tom'}

dict_1 = {'foo': 'bar', 'bar': 'buz'}
dict_2 = {'dou': 'jones', 'USD': 36}
dict_3 = {'AUD': 19.2, 'name': 'Tom'}

dict_list = [dict_2, dict_3]

for dictionary in dict_list:
	dict_1.update(dictionary)

print(dict_1)
