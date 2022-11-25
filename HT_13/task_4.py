#  Створіть клас, який буде повністю копіювати поведінку list, за виключенням того, що індекси в ньому мають
#  починатися з 1, а індекс 0 має викидати помилку (такого ж типу, яку кидає list якщо звернутися до неіснуючого
#  індексу)

class NewList(list):

    def __getitem__(self, item):
        #print('Test __getitem__!')
        if item < 0:
            return super(NewList, self).__getitem__(item)
        elif item > 0:
            return super(NewList, self).__getitem__(item - 1)
        else:
            raise IndexError('list index out of range')


a = []
print('Regular list test:')
a.append('01')
a.append('02')
a.append('03')

print(f'a[0] -> {a[0]}')
print(f'a[1] -> {a[1]}')
print(f'a[2] -> {a[2]}')

print(f'a[-1] -> {a[-1]}')
print(f'a[-2] -> {a[-2]}')
print(f'a[-3] -> {a[-3]}')

print('New list test:')
b = NewList()
b.append('01')
b.append('02')
b.append('03')


print(f'b[1] -> {b[1]}')
print(f'b[2] -> {b[2]}')
print(f'b[3] -> {b[3]}')

print(f'b[-1] -> {b[-1]}')
print(f'b[-2] -> {b[-2]}')
print(f'b[-3] -> {b[-3]}')

print(f'b[0] -> {b[0]}')

