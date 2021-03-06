"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 23.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 30/11/2020
Дата последней модификации: 30/11/2020
Описание: Решение задачи 23 практикума № 1
#версия Python: 3.8
"""

"""
Даны вещественные числа X и Y . Вычислить Z = √(X x Y) при X > Y,
Z = ln(X + Y) в противном случае.
"""
import math
X = float(input("Введите вещественное число X:"))
Y = float(input("Введите вещественное число Y:"))
if X>Y:
    Z = math.sqrt(X*Y)
    print(Z)
else:
    Z=math.log(X+Y, math.e)
    print(Z)
