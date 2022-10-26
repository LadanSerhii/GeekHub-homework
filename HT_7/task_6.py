# Напишіть функцію,яка приймає рядок з декількох слів і повертає довжину найкоротшого слова. Реалізуйте обчислення
# за допомогою генератора в один рядок.

def smallest_word(user_str):
    return min(list((len(el) for el in user_str.split())))


print(smallest_word(input()))
