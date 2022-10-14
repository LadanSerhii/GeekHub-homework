# Користувачем вводиться початковий і кінцевий рік. Створити цикл, 
# який виведе всі високосні роки в цьому проміжку (границі включно). 
# P.S. Рік є високосним, якщо він кратний 4, але не кратний 100, 
# а також якщо він кратний 400.

number_1, number_2 = input('Please input 2 years separated by \
whitespace: ').split()
number_1 = int(number_1)
number_2 = int(number_2)
for year in range(number_1, number_2 + 1):
	if (not year % 4 and year % 100) or not year % 400:
		print(year)
