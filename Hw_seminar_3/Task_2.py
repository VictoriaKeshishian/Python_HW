# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

list_dupl = [1, 2, 3] * 3
result_list = []
for item in list_dupl:
    if item not in result_list:
        result_list.append(item)

print(result_list)

