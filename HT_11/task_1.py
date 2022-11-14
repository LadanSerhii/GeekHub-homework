# 1. Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції
# з 2-ма числами, а саме додавання, віднімання, множення, ділення.
# - Якщо під час створення екземпляру класу звернутися до атрибута last_result він повинен повернути пусте значення.
# - Якщо використати один з методів - last_result повинен повернути результат виконання ПОПЕРЕДНЬОГО методу.
#     Example:
#     last_result --> None
#     1 + 1
#     last_result --> None
#     2 * 3
#     last_result --> 2
#     3 * 4
#     last_result --> 6
#     ...
# - Додати документування в клас (можете почитати цю статтю:
# https://realpython.com/documenting-python-code/ )

class Calc(object):
    """The class modeling the basic functions of calculator"""
    last_result = None
    tmp_result = None

    def plus(self, num_1, num_2):
        """ADD function"""
        self.last_result = self.tmp_result
        self.tmp_result = num_1 + num_2
        return self.tmp_result

    def minus(self, num_1, num_2):
        """MINUS function"""
        self.last_result = self.tmp_result
        self.tmp_result = num_1 - num_2
        return self.tmp_result

    def mult(self, num_1, num_2):
        """MULTIPLICATION function"""
        self.last_result = self.tmp_result
        self.tmp_result = num_1 * num_2
        return self.tmp_result

    def div(self, num_1, num_2):
        """DIVISION function"""
        self.last_result = self.tmp_result
        if num_2:
            self.tmp_result = num_1 / num_2
        else:
            self.tmp_result = None
        return self.tmp_result


calc = Calc()
print(calc.last_result)
calc.plus(1, 1)
print(calc.last_result)
calc.mult(2, 3)
print(calc.last_result)
calc.mult(3, 4)
print(calc.last_result)
calc.div(1, 0)
print(calc.last_result)
calc.minus(10, 1)
print(calc.last_result)
calc.div(4, 2)
print(calc.last_result)
calc.plus(4, 2)
print(calc.last_result)
