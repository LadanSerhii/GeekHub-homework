# 1. Напишіть програму, де клас «геометричні фігури» (Figure) містить властивість color з початковим значенням white
# і метод для зміни кольору фігури, а його підкласи «овал» (Oval) і «квадрат» (Square) містять методи _init_ для
# завдання початкових розмірів об'єктів при їх створенні.

class Figure(object):
    color = 'white'

    def change_color(self, color):
        self.color = color


class Oval(Figure):
    def __init__(self, dim_1, dim_2):
        print(f'This is {self.color} oval with {dim_1} and {dim_2} dimensions!' )


class Square(Figure):
    def __init__(self, side):
        print(f'This is {self.color} square with {side} dimension!')


ov = Oval(7, 167)
sq = Square(260)

ov.change_color('red')
sq.change_color('green')

print(f'The oval color changed to {ov.color}!')
print(f'The square color changed to {sq.color}!')

