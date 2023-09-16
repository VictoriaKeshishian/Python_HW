# ✔ Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if (number % i == 0):
            return False
    return True

def prime_numbers():
    count = 0
    number = 2
    while count < number:
        if is_prime(number):
            yield number
            count += 1
        number += 1

# не забываем самостоятельно останавливать !
print("Генерация простых чисел:")
for prime in prime_numbers():
    print(prime)




