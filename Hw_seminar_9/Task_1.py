# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import math
import csv
import random
import json
import os
from functools import wraps

def find_roots(a, b, c):
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
    if dis > 0:
        root1 = (-b + sqrt_val) / (2 * a)
        root2 = (-b - sqrt_val) / (2 * a)
        return [root1, root2]
    elif dis == 0:
        root = -b / (2 * a)
        return [root]
    else:
        real_part = -b / (2 * a)
        imaginary_part = sqrt_val / (2 * a)
        root1 = f"{real_part} + {imaginary_part}i"
        root2 = f"{real_part} - {imaginary_part}i"
        return [root1, root2]

def generate_csv_file():
    if not os.path.isfile("test.csv"):
        with open("test.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["a", "b", "c"])
            for _ in range(random.randint(100, 1000)):
                row = [random.randint(1, 10) for _ in range(3)]
                writer.writerow(row)

def decorator_roots(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not os.path.isfile("test.csv"):
            generate_csv_file()
        with open("test.csv", "r", newline='') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                a, b, c = map(int, row)
                func(a, b, c)
    return wrapper

def decorator_result(func):
    @wraps(func)
    def wrapper(a, b, c):
        result = func(a, b, c)
        data = {
            "параметры": {"a": a, "b": b, "c": c},
            "корни": result
        }
        if not os.path.isfile("result.json"):
            result_data = [data]
        else:
            with open("result.json", "r", newline='', encoding='utf-8') as f_json:
                result_data = json.load(f_json)
            result_data.append(data)
        with open("result.json", "w", newline='', encoding='utf-8') as f_json:
            json.dump(result_data, f_json, indent=4, ensure_ascii=False)
        return result
    return wrapper
@decorator_roots
@decorator_result
def new_func(a, b, c):
    return find_roots(a, b, c)

new_func()