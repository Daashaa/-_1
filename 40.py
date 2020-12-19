"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 40.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 01/12/2020
Дата последней модификации: 01/12/2020
Описание: Решение задачи 40 практикума № 1
#версия Python: 3.8
"""

"""
Дан одномерный массив числовых значений, насчитывающий N элементов. После каждого
отрицательного элемента вставить новый элемент, равный квадрату этого отрицательного
элемента.
"""
import random
N = int(input("Введите количество элементов массива: "))
a = [random.randint(-100, 100) for i in range(N)]
print(a)
for i in range(N):
    if a[i] < 0:
        a[i] = a[i], a[i]**2
print(a)
