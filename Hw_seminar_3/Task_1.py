# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

def find_all_items(hike_friends):
    all_things = set()

    for friend, things in hike_friends.items():
        all_things.update(things)

    return all_things


def find_unique_items(hike_friends):
    unique_items = set()
    non_unique_items = set()

    for items in hike_friends.values():
        for item in items:
            if item in unique_items:
                non_unique_items.add(item)
            else:
                unique_items.add(item)

    unique_items = unique_items - non_unique_items

    unique_items_per_friend = {}
    for friend, items in hike_friends.items():
        unique_items_friend_has = unique_items.intersection(items)
        if unique_items_friend_has:
            unique_items_per_friend[friend] = unique_items_friend_has

    return unique_items_per_friend

def find_things(hike_friends):
    items_count = {}

    for items in hike_friends.values():
        for item in items:
            if item in items_count:
                items_count[item] += 1
            else:
                items_count[item] = 1

    missing_items = {}
    for name, items in hike_friends.items():
        missing = set()
        for item in items_count:
            if items_count[item] == len(hike_friends) - 1 and item not in items:
                missing.add(item)
        if missing:
            missing_items[name] = missing

    return missing_items

hike_friends = {'Олег': ('Палатка', 'Рюкзак', 'Компас', 'Спальник', 'Горелка'),
                'Саша': ('Палатка', 'Рюкзак', 'Нож', 'Гитара', 'Сух.паёк'),
                'Андрей': ('Чайник', 'Рюкзак', 'Бинт', 'Фонарик', 'Сух.паёк'),
                'Василий': ('Палатка', 'Топор', 'Карта', 'Вода', 'Спички')}

all_items = find_all_items(hike_friends)
print('Все вещи: \n' + '\n'.join(all_items))
print('_________________')
print('Уникальные вещи')
unique_items = find_unique_items(hike_friends)
for friend, items in unique_items.items():
    print(f"{friend}: {', '.join(items)}")

print('_________________')
print('')

missing_items = find_things(hike_friends)

for friend, items in missing_items.items():
    print(f"Вещи, которые есть у всех, кроме {friend}: {', '.join(items)}")



