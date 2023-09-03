# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
def guess_number():
    for guess_made in range(10):
        number = int(input("Угадай число: "))
        if number > num:
            print("Число больше загаданного ")
        elif number < num:
            print("Число меньше загаданного ")
        else:
            print("Вы угадали число!")
            break
        difference = abs(number - num)
        if difference < 10:
            print("но очень близко!")
        elif difference < 50:
            print("и находится близко, но не совсем")
        elif difference < 100:
            print(" и довольно далеко от истины")
    else:
        print(f"Вы не угадали число. Загаданное число было {num}")

guess_number()
