# Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції. Тобто щоб її можна було використати
# у вигляді:
#     for i in my_range(1, 10, 2):
#         print(i)
#     1
#     3
#     5
#     7
#     9
#    P.S. Повинен вертатись генератор.
#    P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній:
#    https://docs.python.org/3/library/stdtypes.html#range
#    P.P.P.S Не забудьте обробляти невалідні ситуації (типу range(1, -10, 5) тощо).
#    Подивіться як веде себе стандартний range в таких випадках.

def new_range(*args):
    if len(args) == 1:
        start = 0
        finish = args[0]
        step = 1
    elif len(args) == 2:
        start = args[0]
        finish = args[1]
        step = 1
    elif len(args) == 3:
        start = args[0]
        finish = args[1]
        step = args[2]
    else:
        raise Exception('The number of args should be 1 to 3!')

    if step > 0:
        value = start
        while value < finish:
            yield value
            value += step
    else:
        value = start
        while value > finish:
            yield value
            value += step


try:
    print(list(new_range(10)))
    print(list(range(10)))
    print(list(new_range(10, 15)))
    print(list(range(10, 15)))
    print(list(new_range(10, 15, 2)))
    print(list(range(10, 15, 2)))
    print(list(new_range(1, 1, 1, 1)))
    print(list(new_range()))
except Exception as e:
    print(e)
