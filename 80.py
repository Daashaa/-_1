"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 80.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 24/03/2021
Дата последней модификации: 24/03/2021
Описание: Решение задачи 80 практикума № 1
#версия Python: 3.9
"""

"""
Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
Разделить элементы матрицы на элемент матрицы с наибольшим значением.
"""
import random
N = int(input("Введите количество строк: "))
M = int(input("Введите количество столбцов: "))
def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(0, 99))
    return col
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
def get_column(matrix, index):
    column = []
    i = 0
    while i < len(matrix):
        column.append(matrix[i][index])
        i += 1
    return column
A = get_matrix(N, M)
print("Исходная матрица:")
print_matrix(A)
max_element = False
i = 0
while i < len(A):
    j = 0
    while j < len(A[i]):
        if max_element is False or max_element < A[i][j]:
            max_element = A[i][j]
        j += 1
    i += 1
i = 0
while i < len(A):
    j = 0
    while j < len(A[i]):
        A[i][j] /= max_element
        A[i][j] = round(A[i][j], 1)
        j += 1
    i += 1
print("Максимальный элемент:", max_element)
print("Модифицированная матрица:")
print_matrix(A)
