# Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def func(**kwargs):
    arg_dict = {}
    for key, value in kwargs.items():
        try:
            arg_dict[value] = key
        except:
            arg_dict[str(value)] = key
    return arg_dict

result = func(a=5, b='hello', c=[1, 2, 3])
print(result)

