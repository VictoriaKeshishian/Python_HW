# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY.
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.


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


