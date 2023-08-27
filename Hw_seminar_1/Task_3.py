# Напишите код, который запрашивает число и сообщает, является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def prime_number(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

while True:
    try:
        number = int(input('Введите число от 2 до 100 000: '))
        if 2 <= number <= 100000:
            if prime_number(number):
                print(f'{number} - это простое число.')
            else:
                print(f'{number} - это составное число.')
            break
        else:
            print('Пожалуйста, введите число в диапазоне от 2 до 100000.')
    except ValueError:
        print('Пожалуйста, введите целое число.')





