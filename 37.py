"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 37.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 01/12/2020
Дата последней модификации: 01/12/2020
Описание: Решение задачи 37 практикума № 1
#версия Python: 3.8
"""

"""
Дан одномерный массив числовых значений, насчитывающий N элементов. Сумму элементов
массива и количество положительных элементов поставить на первое и второе место.
"""
import array
import random
N = int(input("Введите количество элементов массива: "))
a = [random.randint(-100, 100) for i in range(N)]
print(a)
b = 0
s = sum(a)
for i in range(N):
    if a[i] >= 0:
        b += 1
(a.insert(0, s))
(a.insert(1, b))
print(a)
