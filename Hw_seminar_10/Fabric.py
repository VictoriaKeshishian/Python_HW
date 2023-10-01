
# Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
from Animal import Fish, Mammal, Bird, Cat
class Fabric:
    @staticmethod
    def get_animal(animal_type: str, *args, **kwargs):
        if animal_type == "Fish":
            return Fish(*args, **kwargs)
        if animal_type == "Mammal":
            return Mammal(*args, **kwargs)
        if animal_type == "Bird":
            return Bird(*args, **kwargs)
        if animal_type == "Cat":
            return Cat(*args, **kwargs)



cat = Fabric.get_animal("Cat", "Barsic", age=5, weight=3)
bird = Fabric.get_animal("Bird", "Gosha", age=1, feather='перстрое')

print(f"Имя: {cat.get_name()}, Возраст: {cat.get_age()}, Особенности: {cat.get_specific()}")
print(f"Имя: {bird.get_name()}, Возраст: {bird.get_age()}, Особенности: {bird.get_specific()}")


