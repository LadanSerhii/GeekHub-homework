# Write a script which accepts two sequences of comma-separated 
# colors from user. Then print out a set containing all the colors 
# from color_list_1 which are not present in color_list_2


color_list_1 = (input().split(','))
color_list_2 = (input().split(','))
for color in color_list_1:
	if color not in color_list_2:
		print(color)
