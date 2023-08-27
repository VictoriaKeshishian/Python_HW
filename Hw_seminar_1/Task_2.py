# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

def is_triangle(side_a, side_b, side_c):
    return side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a

def type_triangle(side_a, side_b, side_c):
    if is_triangle(side_a, side_b, side_c):
        if side_a == side_b or side_b == side_c or side_c == side_a:
            return 'Это равнобедренный треугольник'
        elif side_a == side_b == side_c:
            return 'Это равносторонний треугольник'
        else:
            return 'Это разносторонний треугольник'
    else:
        return 'Треугольника с такими сторонами не существует!'

side_a = int(input('Введите значение стороны а: '))
side_b = int(input('Введите значение стороны b: '))
side_c = int(input('Введите значение стороны c: '))

print(type_triangle(side_a, side_b, side_c))