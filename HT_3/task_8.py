# Створити цикл від 0 до ... (вводиться користувачем). 
# В циклі створити умову, яка буде виводити поточне значення, 
# якщо остача від ділення на 17 дорівнює 0.

number = int(input('Please input a numeber: '))

for num in range(number + 1):
	if not num % 17:
		print(num)
