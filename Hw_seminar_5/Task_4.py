# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fib(k):
    a, b = 0, 1
    for _ in range(k):
        yield a
        a, b = b, a + b

fibonacci_generator = fib(6)

for number in fibonacci_generator:
    print(number)