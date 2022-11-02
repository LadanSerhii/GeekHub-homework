# Програма-світлофор.
#    Створити програму-емулятор світлофора для авто і пішоходів. Після запуска програми на екран виводиться в
#    лівій половині - колір автомобільного, а в правій - пішохідного світлофора. Кожну 1 секунду виводиться поточні
#    кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах
#    (пішоходам зелений тільки коли автомобілям червоний).
#    Приблизний результат роботи наступний:
#       Red        Green
#       Red        Green
#       Red        Green
#       Red        Green
#       Yellow     Red
#       Yellow     Red
#       Green      Red
#       Green      Red
#       Green      Red
#       Green      Red
#       Yellow     Red
#       Yellow     Red
#       Red        Green

import time


def color_p(color_a):
    if color_a == 'Green' or color_a == 'Yellow':
        return 'Red'
    else:
        return 'Green'


def color_print(color_a):
    print(f'{color_a} \t {color_p(color_a)}')


def color_switch(color):
    if color == 'Red':
        return 'Green'
    else:
        return 'Red'


def color_iter(color_a, iter_amount=6, tm=1):
    for i in range(2 * (iter_amount // 3)):
       color_print(color_a)
       time.sleep(tm)
    for i in range(iter_amount // 3):
        color_print('Yellow')
        time.sleep(tm)


color_a = 'Red'
while(1):
    color_iter(color_a)
    color_a = color_switch(color_a)



