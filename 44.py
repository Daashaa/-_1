"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 44.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 04/12/2020
Дата последней модификации: 04/12/2020
Описание: Решение задачи 44 практикума № 1
#версия Python: 3.8
"""

"""
Дан одномерный массив числовых значений, насчитывающий N элементов.
Добавить столько элементов, чтобы элементов с положительными и
отрицательными значениями стало бы поровну.
"""
import random
N = int(input("Введите количество элементов массива: "))
A = [random.randint(-100, 100) for i in range(N)]
print(A)
n = []
p = []
for i in range(N):
    if A[i] > 0:
        p.append(A[i])
    else:
        n.append(A[i])
sn=len(n)
sp=len(p)
Q = sn-sp
W = sp - sn
print("Количество отрицательных элементов:", sn)
print("Количество положительных элементов:", sp)
if sn == sp:
    print("Количество отрицательных и положительных элементов массива равно")
if sn > sp:
    A.append([random.randint(1,100) for i in range(Q)])
if sp > sn:
    A.append([random.randint(-1, -100) for i in range(W)])
print(A)
