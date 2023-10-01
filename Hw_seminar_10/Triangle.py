class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def is_triangle(self):
        return self.side_a + self.side_b > self.side_c and self.side_a + self.side_c > self.side_b and self.side_b + self.side_c > self.side_a

    def type_triangle(self):
        if self.is_triangle():
            if self.side_a == self.side_b and self.side_b == self.side_c:
                return 'Это равносторонний треугольник'
            elif self.side_a == self.side_b or self.side_b == self.side_c or self.side_c == self.side_a:
                return 'Это равнобедренный треугольник'
            else:
                return 'Это разносторонний треугольник'
        else:
            return 'Треугольника с такими сторонами не существует!'

if __name__ == "__main__":
    side_a = int(input('Введите значение стороны а: '))
    side_b = int(input('Введите значение стороны b: '))
    side_c = int(input('Введите значение стороны c: '))

    triangle = Triangle(side_a, side_b, side_c)
    result = triangle.type_triangle()
    print(result)
