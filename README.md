# Задачи к семинару 1:
1. Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
2. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. 
Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
то треугольника с такими сторонами не существует. Отдельно сообщить является ли 
треугольник разносторонним, равнобедренным или равносторонним.
3. Напишите код, который запрашивает число и сообщает, является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
>from random import randint 
> 
>num = randint(LOWER_LIMIT, UPPER_LIMIT)
***
# Задачи к семинару 2:

1. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
строковое представление. Функцию hex используйте для проверки своего результата.
2. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
***
# Задачи к семинару 3:
1. Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
- Какие вещи взяли все три друга
- Какие вещи уникальны, есть только у одного друга
- Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
- Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания
и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
***
# Задачи к семинару 4:
1. Напишите функцию для транспонирования матрицы
2. Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь, 
где ключ — значение переданного аргумента, а значение — имя аргумента. 
Если ключ не хешируем, используйте его строковое представление
3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте 
все операции поступления и снятия средств в список.

***
# Задачи к семинару 5:
1. Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2. Для проверки числа на простоту 
используйте правило: «число является простым, если делится нацело только на единицу и на себя».
2. Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
3. На вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии
4. Создайте функцию генератор чисел Фибоначчи (см. Википедию)

***
# Задачи к семинару 6:
1. Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY Функция возвращает истину, 
если дата может существовать или ложь, если такая дата невозможна. Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. Проверку года на високосность 
вынести в отдельную защищённую функцию.
2. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. 
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, 
определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, 
каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
4. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

***
# Задачи к семинару 7:

1. Решить задачи, которые не успели решить на семинаре.
2. Напишите функцию группового переименования файлов. Она должна:
* принимать параметр желаемое конечное имя файлов. 
При переименовании в конце имени добавляется порядковый номер.
* принимать параметр количество цифр в порядковом номере.
* принимать параметр расширение исходного файла. 
Переименование должно работать только для этих файлов внутри каталога.
* принимать параметр расширение конечного файла.
* принимать диапазон сохраняемого оригинального имени. 
* _Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
К ним прибавляется желаемое конечное имя, если оно передано. 
Далее счётчик файлов и расширение._ 
3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

***
# Задачи к семинару 8:

1. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
Для дочерних объектов указывайте родительскую директорию.
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

***
# Задачи к семинару 9:
1. Напишите следующие функции:
* Нахождение корней квадратного уравнения
* Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
* Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
* Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

2. Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

***
# Задачи к семинару 10:

1. Создайте класс-фабрику.
* Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
* Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
2. Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали. 
Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра.