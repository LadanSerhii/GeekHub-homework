# Write a script which accepts two sequences of comma-separated 
# colors from user. Then print out a set containing all the colors 
# from color_list_1 which are not present in color_list_2


color_set_1 = set((input('Please input 1st color list: ').split(',')))
color_set_2 = set((input('Please input 2nd color list: ').split(',')))

final_set = color_set_1.difference(color_set_2)
print(final_set)
