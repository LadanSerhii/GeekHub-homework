#  Запишіть в один рядок генератор списку (числа в діапазоні від 0 до 100 не включно), сума цифр кожного елемент якого
#  буде дорівнювати 10.
#    Результат: [19, 28, 37, 46, 55, 64, 73, 82, 91]


gen = [i for i in range(100) if (i - (i//10)*10 + (i//10)) == 10]

print(gen)