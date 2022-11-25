# 2. Створити клас Matrix, який буде мати наступний функціонал:
# 1. __init__ - вводиться кількість стовпців і кількість рядків
# 2. fill() - заповнить створений масив числами - по порядку. Наприклад:
# +────+────+
# | 1  | 2  |
# +────+────+
# | 3  | 4  |
# +────+────+
# | 5  | 6  |
# +────+────+
# 3. print_out() - виведе створений масив (якщо він ще не заповнений даними - вивести нулі
# 4. transpose() - перевертає створений масив. Тобто, якщо взяти попередню таблицю, результат буде
# +────+────+────+
# | 1  | 3  | 5  |
# +────+────+────+
# | 2  | 4  | 6  |
# +────+────+────+
# P.S. Всякі там Пандас/Нампай не використовувати - тільки хардкор ;)
# P.P.S. Вивід не обов’язково оформлювати у вигляді таблиці - головне, щоб було видно, що це окремі стовпці / рядки


class Matrix(object):
    rows = []
    cols = []

    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols

        for el_r in range(self.n_cols):
            for el_c in range(self.n_rows):
                self.rows.append(0)
            self.cols.append(self.rows)
            self.rows = []

    def fill(self):
        self.cols = []
        self.rows = []
        for el_r in range(self.n_cols):
            for el_c in range(self.n_rows):
                self.rows.append(el_c + el_r * self.n_rows + 1)
            self.cols.append(self.rows)
            self.rows = []

    def print_out(self):
        max_len = 0
        for c in self.cols:
            for r in c:
                if len(str(r)) > max_len:
                    max_len = len(str(r))
        for c in self.cols:
            for r in c:
                element_to_print = str(r)
                print(f'[{element_to_print.center(max_len + 2)}]', end='')
            print('\n', end='')

    def transpose(self):
        tmp_rows = []
        tmp_cols = []
        for index in range(self.n_rows):
            for el in self.cols:
                tmp_rows.append(el[index])
            tmp_cols.append(tmp_rows)
            tmp_rows = []
        self.cols = tmp_cols


mx = Matrix(5, 3)
mx.print_out()
mx.transpose()
mx.print_out()
mx_1 = Matrix(4, 2)
mx_1.fill()
mx_1.print_out()
mx_1.transpose()
mx_1.print_out()
