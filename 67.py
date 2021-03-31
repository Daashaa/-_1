"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 67.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 20/03/2021
Дата последней модификации: 20/03/2021
Описание: Решение задачи 67 практикума № 1
#версия Python: 3.8
"""

"""
Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
Найти наибольший элемент столбца матрицы A, для которого сумма абсолютных значений элементов
максимальна.
"""
import random
N = int(input("Введите количество строк: "))
M = int(input("Введите количество столбцов: "))
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
def listsum(list):
    sum = 0
    for element in list:
        sum += element
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
tmp = list(zip(*A))
maxsum = 0
columnmax = 0
i = 0
while i < len(tmp):
    column = tmp[i]
    current_list_sum = listsum(column)
    if current_list_sum > maxsum:
        maxsum = current_list_sum
        columnmax = i
    i += 1
print("Матрица:")
print_matrix(A)
print("Cтолбец для которого сумма абсолютных значений элементов максимальна:",
      columnmax)
print("Наибольший элемент этого столбца:", max(tmp[columnmax]))
