# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

for row in range(2, 11):
    for col in range(2, 6):
        result = col * row
        print(f'{col:2} * {row:2} = {result:2}', end=' ' * 4)
    print()

print()

for row in range(2, 11):
    for col in range(6, 10):
        result = col * row
        if col == 9:
            print(f'{col:2} * {row:2} = {result:2}', end=' ')
        else:
            print(f'{col:2} * {row:2} = {result:2}', end=' ' * 4)
    print()