"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 66.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 20/03/2021
Дата последней модификации: 20/03/2021
Описание: Решение задачи 66 практикума № 1
#версия Python: 3.8
"""

"""
Для вводимых чисел определить процент положительных и отрицательных чисел.
При вводе числа −65432 закончить работу.
"""
import re
list_numbers = []
pos = 0
neg = 0
while True:
    print("Введите число:", end=' ')
    string = re.sub(r'[^0-9\-]+', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа")
        continue
    n = int(string)
    if n * -1 == 65432:
        break
    list_numbers.append(n)
    if n < 0:
        neg += 1
    else:
        pos += 1
pr = 100 / len(list_numbers)
print("Процент положительных чисел:", pr * pos)
print("Процент отрицательных чисел:", pr * neg)
