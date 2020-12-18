"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 19.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 30/11/2020
Дата последней модификации: 30/11/2020
Описание: Решение задачи 19 практикума № 1
#версия Python: 3.8
"""

"""
Даны вещественные числа: X, Y, Z. Определить, существует ли треугольник
с такими длинами сторон и, если существует, будет ли он прямоугольным.
"""
X = int(input("Сторона 1:"))
Y = int(input("Сторона 2:"))
Z = int(input("Сторона 3:"))
if (X+Y<=Z) or (Y+Z<=X) or (X+Z<=Y):
    print("Треугольник с такими сторонами не существует")
    import sys
    sys.exit(0)
if (X>Y and X>Z) and (X**2==Y**2+Z**2):
    print("Треугольник прямоугольный")
elif (Y>X and Y>Z) and (Y**2==X**2+Z**2):
    print("Треугольник прямоугольный")
elif (Z>X and Z>Y) and (Z**2==X**2+Y**2):
    print("Треугольник прямоугольный")
else:
    print("Треугольник не прямоугольный")
