class Animal:
    def __init__(self, type, age):
        self.__name, self.__age = type, age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class Fish(Animal):

    def __init__(self, type, age, color):
        super().__init__(type, age)
        self.__name, self.__age = type, age
        self.__color = color

    def get_specific(self):
        return (f"Цвет: {self.__color}")


class Mammal(Animal):

    def __init__(self, type, age, wool):
        super().__init__(type, age)
        self.__name, self.__age = type, age
        self.__wool = wool

    def get_specific(self):
        return (f"Пушистость: {self.__wool}")


class Bird(Animal):

    def __init__(self, type, age, feather):
        super().__init__(type, age)
        self.__name, self.__age = type, age
        self.__feather = feather

    def get_specific(self):
        return (f"Оперение: {self.__feather}")

class Cat(Animal):
    def __init__(self, type, age, weight):
        super().__init__(type, age)
        self.__name, self.age = type, age
        self.__weight = weight

    def get_specific(self):
        return (f"Вес: {self.__weight}")

