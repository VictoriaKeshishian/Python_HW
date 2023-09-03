# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import math
from fractions import Fraction

def parse_fraction(fraction_str):
    numerator, denominator = map(int, fraction_str.split('/'))
    return numerator, denominator

def sum_fractions(fraction1, fraction2):
    numerator1, denominator1 = fraction1
    numerator2, denominator2 = fraction2

    sum_numerators = (numerator1*denominator2) + (numerator2*denominator1)
    mult_denominators = denominator1 * denominator2
    gcd_value = math.gcd(sum_numerators, mult_denominators)
    sum_numerators //= gcd_value
    mult_denominators //= gcd_value
    return sum_numerators, mult_denominators

def mult_fractions (fraction1, fraction2):
    numerator1, denominator1 = fraction1
    numerator2, denominator2 = fraction2

    sum_numerators = numerator1 * numerator2
    mult_denominators = denominator1 * denominator2
    gcd_value = math.gcd(sum_numerators, mult_denominators)
    sum_numerators //= gcd_value
    mult_denominators //= gcd_value
    return sum_numerators, mult_denominators

fraction_num = input("Введите дробное число формата a/b: ")
fraction_num_2 = input("Введите второе дробное число формата a/b: ")

fraction1 = parse_fraction(fraction_num)
fraction2 = parse_fraction(fraction_num_2)

# сложение дробей
sum_fraction = sum_fractions(fraction1, fraction2)
# умножение дробей
mult_fraction = mult_fractions(fraction1, fraction2)
# Вывод результатов
print(f"Сумма дробей: {sum_fraction[0]}/{sum_fraction[1]}")
print(f"Произведение дробей: {mult_fraction[0]}/{mult_fraction[1]}")

# Проверка
fraction1 = Fraction(fraction_num)
fraction2 = Fraction(fraction_num_2)

# Сложение дробей
sum_fraction = fraction1 + fraction2

# Умножение дробей
product_fraction = fraction1 * fraction2

# Вывод результатов
print(f"Модуль fraction: Сумма дробей: {sum_fraction.numerator}/{sum_fraction.denominator}")
print(f"Модуль fraction: Произведение дробей: {product_fraction.numerator}/{product_fraction.denominator}")

