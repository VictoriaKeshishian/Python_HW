# ✔ Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

list_names = ['Valya', 'Anna', 'Elena']
list_salary = [35, 25, 50]
list_prize = ['0.5', '0.3', '0.8']

def dict_salary(list_names, list_salary, list_prize):
    float_prize = [float(value) for value in list_prize]
    sum_prize = []
    for i in range(0, len(list_salary)):
        sum_prize.append(list_salary[i] * float_prize[i])
    myDict = {list_names[i]: sum_prize[i] for i in range(0, len(list_names))}
    print(myDict)

dict_salary(list_names, list_salary, list_prize)