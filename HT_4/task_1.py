def seasons(month):
	if month in range(1, 3) or month == 12:
		return 'Winter'
	elif month in range(3, 6):
		return 'Spring '
	elif month in range(6, 9):
		return 'Summer'
	elif month in range(9, 12):
		return 'Autumn'
	else:
		return 'Wrong input!'

month = int(input('Please eneter # of month: '))
print(seasons(month))
