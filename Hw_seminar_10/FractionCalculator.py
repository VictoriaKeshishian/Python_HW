import math
from fractions import Fraction


class FractionCalculator:
    def __init__(self):
        self.fraction1 = None
        self.fraction2 = None

    def parse_fraction(self, fraction_str):
        numerator, denominator = map(int, fraction_str.split('/'))
        return numerator, denominator

    def set_fractions(self):
        fraction_num = input("Введите дробное число формата a/b: ")
        fraction_num_2 = input("Введите второе дробное число формата a/b: ")

        self.fraction1 = self.parse_fraction(fraction_num)
        self.fraction2 = self.parse_fraction(fraction_num_2)

    def sum_fractions(self):
        numerator1, denominator1 = self.fraction1
        numerator2, denominator2 = self.fraction2

        sum_numerators = (numerator1 * denominator2) + (numerator2 * denominator1)
        mult_denominators = denominator1 * denominator2
        gcd_value = math.gcd(sum_numerators, mult_denominators)
        sum_numerators //= gcd_value
        mult_denominators //= gcd_value
        return sum_numerators, mult_denominators

    def mult_fractions(self):
        numerator1, denominator1 = self.fraction1
        numerator2, denominator2 = self.fraction2

        sum_numerators = numerator1 * numerator2
        mult_denominators = denominator1 * denominator2
        gcd_value = math.gcd(sum_numerators, mult_denominators)
        sum_numerators //= gcd_value
        mult_denominators //= gcd_value
        return sum_numerators, mult_denominators

    def calculate(self):
        self.set_fractions()

        # сложение дробей
        sum_fraction = self.sum_fractions()
        # умножение дробей
        mult_fraction = self.mult_fractions()


        # Проверка с использованием fractions.Fraction
        fraction1 = Fraction(f"{self.fraction1[0]}/{self.fraction1[1]}")
        fraction2 = Fraction(f"{self.fraction2[0]}/{self.fraction2[1]}")

        # Сложение дробей
        sum_fraction = fraction1 + fraction2

        # Умножение дробей
        product_fraction = fraction1 * fraction2

        print(f"Модуль fraction: Сумма дробей: {sum_fraction.numerator}/{sum_fraction.denominator}")
        print(f"Модуль fraction: Произведение дробей: {product_fraction.numerator}/{product_fraction.denominator}")


if __name__ == "__main__":
    calculator = FractionCalculator()
    calculator.calculate()
