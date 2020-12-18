"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 31.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 30/11/2020
Дата последней модификации: 30/11/2020
Описание: Решение задачи 31 практикума № 1
#версия Python: 3.8
"""

"""
Нарисуйте полную блок-схему алгоритма сортировки массива «методом пузырька».
"""
import random
dim = 20
arr = [random.randint(0, 100) for i in range(dim)]
print(arr)
n=1
while n < dim:
    for i in range(dim - n):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    n += 1
print(arr)
