# Написати функцію, яка приймає на вхід список (через кому), підраховує кількість однакових елементів у ньому і
# виводить результат. Елементами списку можуть бути дані будь-яких типів.
#     Наприклад:
#     1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"


def count_elements(*args):
    lst = []
    for el in args:
        lst.append(el)
    lst_1 = list(map(str, lst))
    unique_elements = []
    freq = []
    for element in lst_1:
        if element not in unique_elements and type(element):
            unique_elements.append(element)
            freq.append(lst_1.count(element))

    for element in unique_elements:
        print(f'{element} -> {freq[unique_elements.index(element)]}')


count_elements(1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2])