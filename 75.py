"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 75.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 20/03/2021
Дата последней модификации: 20/03/2021
Описание: Решение задачи 75 практикума № 1
#версия Python: 3.8
"""

"""
Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
Определить, сколько нулевых элементов содержится в верхних L строках матрицы и в левых К столбцах
матрицы.
"""
import random
N = int(input("Введите количество строк: "))
M = int(input("Введите количество столбцов: "))
L = int(input("Введите количество верхних строк: "))
K = int(input("Введите количество левых столбцов: "))
def get_row(column):
    x = []
    for i in range(0, column):
        x.append(random.randint(-9, 9))
    return x
def get_matrix(row, column):
    matrix = []
    for i in range(0, row):
        matrix.append(get_row(column))
    return matrix
def print_matrix(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        row = matrix[i]
        while j < len(row):
            column = row[j]
            print(column, end=' ')
            j += 1
        print()
        i += 1
A = get_matrix(N, M)
print("Исходная матрица:")
print_matrix(A)
l = 0
k = 0
i = 0
while i < len(A):
    j = 0
    while j < len(A[i]):
        if A[i][j] == 0:
            if i < L:
                l += 1
            if j < K:
                k += 1
        j += 1
    i += 1
print("В верхних %s строках содержится %s нулей" % (L, l))
print("В левых %s столбцах содержится %s нулей" % (K, k))
