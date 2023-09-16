# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей
# на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое
# число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

def is_attacking(x1, y1, x2, y2):
    '''
        сравниваем позициии ферзей, x по горизонтали, у по вертикали,
        а также находятся ли ферзи на одной диагонали
    '''
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

def queens_attack(queens):
    '''
       Проходимся по списку с кортежами циклом for, передавая значения кортежа в переменные х и у,
       вызываем функцию is_attacking для проверки позиций и выдаем False в случае если ферзи бьют друг друга
    '''
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            x1, y1 = queens[i]
            x2, y2 = queens[j]
            if is_attacking(x1, y1, x2, y2):
                return False
    return True

# вывод задачи без рандома
# queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
# result = queens_attack(queens)
# print(result)  # Выведет False, так как ферзи (1,1) и (8,8) бьют друг друга
#
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random

def win_queens():
    list_queens = []
    count = 0
    while len(list_queens) < 4 and count <= 10000000000:
        queens = [(i, random.randint(1, 8)) for i in range(1, 9)]
        if queens_attack(queens):
            list_queens.append(queens)
        count += 1
    return list_queens


# вывод задачи с рандомом
successful_setups = win_queens()
for i, queens in enumerate(successful_setups, start=1):
    print(f"Успешная расстановка {i}: {queens}")
