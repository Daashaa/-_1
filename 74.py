"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 74.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 20/03/2021
Дата последней модификации: 20/03/2021
Описание: Решение задачи 74 практикума № 1
#версия Python: 3.8
"""

"""
Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
Определить, сколько отрицательных элементов содержится в каждом столбце и в каждой строке матрицы.
Результат оформить в виде матрицы из N + 1 строк и M + 1 столбцов.
"""
import random
N = int(input("Введите количество строк: "))
M = int(input("Введите количество столбцов: "))
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
def listsum(list):
    sum = 0
    for z in list:
        sum += z
    return sum
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
new_row = []
i = 0
while i < len(A):
    j = 0
    count_row_negative = 0
    while j < len(A[i]):
        is_negative = A[i][j] < 0
        if is_negative:
            count_row_negative += 1
        if len(new_row) <= j:
            new_row.append(1 if is_negative else 0)
        else:
            new_row[j] += 1 if is_negative else 0
        j += 1
    A[i].append(count_row_negative)
    i += 1
A.append(new_row)
print("Модифицированная матрица:")
print_matrix(A)
