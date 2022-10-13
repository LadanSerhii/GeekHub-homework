# Write a script to remove empty elements from a list.
# Test list: [(), ('hey'), ('',), ('ma', 'ke', 'my'), 
# [''], {}, ['d', 'a', 'y'], '', []]

test_list = [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]
test_list_2 = []

for item in test_list:
	if item:
		test_list_2.append(item)
test_list = test_list_2
print(test_list)
