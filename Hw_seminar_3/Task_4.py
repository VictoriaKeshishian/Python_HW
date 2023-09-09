# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

def pack_backpack(items, max_weight):
    result = []

    for item, weight in items.items():
        if weight <= max_weight:
            result.append(item)
            max_weight -= weight

    if result:
        print("Вы можете положить следующие вещи в рюкзак:")
        for item in result:
            print(item)
    else:
        print("Нет предметов, которые могли бы поместиться в рюкзак с заданным весом.")

dict_items = {'Палатка': 10, 'Спальник': 2, 'Чайник': 0.5, 'Фонарик': 0.1, 'Аптечка': 1, 'Вода': 5, 'Топор': 3, 'Еда': 6}
backpack_weight = 21.0

pack_backpack(dict_items, backpack_weight)


