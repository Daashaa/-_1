"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 77.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 20/03/2021
Дата последней модификации: 20/03/2021
Описание: Решение задачи 77 практикума № 1
#версия Python: 3.8
"""

"""
Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
Просуммировать элементы каждой строки матрицы с соответствующими элементами L-й строки.
"""
import random
N = int(input("Введите количество строк: "))
M = int(input("Введите количество столбцов: "))
L = int(input("Введите строку: "))
def get_row(column):
    x = []
    for i in range(0, column):
        x.append(random.randint(0, 9))
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
l = A[L - 1].copy()
i = 0
while i < len(A):
    j = 0
    while j < len(A[i]):
        A[i][j] += l[j]
        j += 1
    i += 1
print("Модифицированная матрица:")
print_matrix(A)
