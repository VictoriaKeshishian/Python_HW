# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from sys import argv

def check_date(full_date: str):
    day, month, year = map(int, full_date.split('.'))
    if 1 <= year <= 9999:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        elif month == 2:
            if 1 <= day <= 28 or leap_year(year):
                return True
        else:
            return False
    return False

def leap_year(year: int):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True

def terminal_date():
    if len(argv) != 2:
        print("Использование: python имя_скрипта.py дд.мм.гггг")
        return False

    date = argv[1]
    return check_date(date)

result = terminal_date()
if result is not None:
    if result:
        print("Дата корректна")
    else:
        print("Дата некорректна")