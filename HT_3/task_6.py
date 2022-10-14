# Write a script to get the maximum and minimum VALUE in a dictionary

test_dict = {
  "one": 4675,
  667: 5560,
  "car": -332,
  "elephant": 9985,
  17: 6653,
  True: 556,
  (1.2, 1.4, 1.5): 10,
  'string': 'string',
  'list': [4, 5, "Pink Floyd"]
}

val_list = []

for element in test_dict:
	if isinstance(test_dict[element], int):
		val_list.append(test_dict[element])
		
print(f'Max value in dictionary: {max(val_list)}')
print(f'Min value in dictionary: {min(val_list)}')
