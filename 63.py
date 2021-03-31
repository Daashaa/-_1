"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 63.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 20/03/2021
Дата последней модификации: 20/03/2021
Описание: Решение задачи 63 практикума № 1
#версия Python: 3.8
"""

"""
Даны число P и число H. Определить сумму чисел меньше P, произведение чисел больше H
и количество чисел в диапазоне значений P и H. При вводе числа равного P или H, закончить работу.
"""
import re
P = int(input("Введите число P: "))
H = int(input("Введите число H: "))
list_numbers = []
s = 0
pr = 1
count = 0
while True:
    print("Введите число:", end=' ')
    string = re.sub(r'[^0-9\-]+', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа")
        continue
    n = int(string)
    list_numbers.append(n)
    if n < P:
        s += n
    elif n > H:
        pr *= n
    if P < H:
        if P < n < H:
            count += 1
    else:
        if H < n < P:
            count += 1
    last_number = list_numbers[len(list_numbers) - 1]
    if last_number == P or last_number == H:
        break
print("Сумма:", s)
print("Произведение:", pr)
print("Количество чисел в диапазоне значений P и H:", count)
