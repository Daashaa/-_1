"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 48.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 04/12/2020
Дата последней модификации: 04/12/2020
Описание: Решение задачи 48 практикума № 1
#версия Python: 3.8
"""

"""
Дан одномерный массив числовых значений, насчитывающий N элементов. Вместо каждого
элемента с нулевым значением поставить сумму двух предыдущих элементов массива.
"""
import random
N = int(input("Введите количество элементов массива: "))
A = [random.randint(-5, 5) for i in range(N)]
print(A)
for i in range(N):
    if A[i] == 0:
        x = A[i-1] + A[i-2]
        A[i] = x
print(A)
