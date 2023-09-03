# ✔ Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

num = int(input("Введите целое число: "))
def sixteen_number(num):
    hex_string = ""
    while num > 0:
        new_num = num % 16
        if new_num < 10:
            hex_string = str(new_num) + hex_string
        else:
            hex_string = chr(ord('A') + new_num - 10) + hex_string
        num //= 16
    return hex_string

hexadecimal = sixteen_number(num)
print("Шестнадцатеричное представление:", hexadecimal)

# Проверка с использованием встроенной функции hex()
hex_builtin = hex(num)
print("Проверка с использованием hex():", hex_builtin)