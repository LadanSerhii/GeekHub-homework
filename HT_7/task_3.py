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

def new_range(start, finish, step=1):
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


print(list(new_range(1, -10, 5)))
print(list(range(1, -10, 5)))

