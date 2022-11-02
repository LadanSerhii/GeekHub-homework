# Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та кількість символів. Файл також додайте в
# репозиторій. На екран має бути виведений список із трьома блоками - символи з початку, із середини та з кінця файлу.
# Кількість символів в блоках - та, яка введена в другому параметрі. Придумайте самі, як обробляти помилку, наприклад,
# коли кількість символів більша, ніж є в файлі або, наприклад, файл із двох символів і треба вивести по одному символу,
# то що виводити на місці середнього блоку символів?). Не забудьте додати перевірку чи файл існує.:

class NumberInMiddle(Exception):
    pass


def file_func(path='task_2.txt', symbol_num=100):
    try:
        with open(path) as file:
            text_0 = file.read()
            file.seek(0)
            try:
                text_1 = file.read(symbol_num)
                if (len(text_0) - symbol_num) // 2 == 0:
                    raise NumberInMiddle
                file.seek((len(text_0) - symbol_num) // 2)
                text_2 = file.read(symbol_num)
                file.seek(len(text_0) - symbol_num)
                text_3 = file.read(symbol_num)
                print(f'First {symbol_num} symbols: {text_1}\nMiddle {symbol_num} symbols: {text_2}\n'
                      f'Last {symbol_num} symbols: {text_3}\n')
            except ValueError:
                print('The symbol number is higher than len of text in file!')
            except NumberInMiddle:
                print('The number of symbols in middle could not be calculated!')
    except FileNotFoundError:
        print('File not found!')


file_func('task_2.txt', 5)