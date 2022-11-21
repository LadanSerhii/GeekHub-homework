# Створіть клас в якому буде атрибут який буде рахувати кількість створених екземплярів класів.

class InstCount(object):
    number_of_inst = 0

    def __init__(self):
        InstCount.number_of_inst += 1


count_1 = InstCount()
print(InstCount.number_of_inst)
count_2 = InstCount()
print(InstCount.number_of_inst)
count_3 = InstCount()
print(InstCount.number_of_inst)