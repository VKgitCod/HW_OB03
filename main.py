class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass
    def eat(self):
        pass

class Bird(Animal):
    def make_sound(self):
        return "Чирррик"

    def fly(self):
        print("Летит")


class Mammal(Animal):
    def make_sound(self):
        return "Мууу"

    def walk(self):
        print("Гуляет")


class Reptile(Animal):
    def make_sound(self):
        return "Шшшшш"

    def crawls(self):
        print("Ползет")

def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} в возрасте {animal.age} издает звук {animal.make_sound()}")



animals = [Bird("Гоша", 1), Mammal("Зорька", 3), Reptile("Нагайна", 8)]

animal_sound(animals)