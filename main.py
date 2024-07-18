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


class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк.")

    def add_staff(self, new_staff):
        self.staff.append(new_staff)
        #return f"Сотрудник {new_staff} принят в зоопарк."
        print(f"Сотрудник {new_staff} принят в зоопарк.")


class ZooKeeper():
    def feed_animal(self, animal):
        print(f"Сотрудник кормит {animal.name}")


class Veterinarian():
    def heal_animal(self, animal):
        print(f"Ветеринар лечит {animal.name}")


def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} в возрасте {animal.age} издает звук {animal.make_sound()}")

#animals = [Bird("Гоша", 1), Mammal("Зорька", 3), Reptile("Нагайна", 8)]
#animal_sound(Zoo.animals)

bird = Bird("Гоша", 1)
mammal = Mammal("Зорька", 3)
reptile = Reptile("Нагайна", 8)

zoo = Zoo()
keeper = ZooKeeper()
veterinarian = Veterinarian()

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zoo.add_staff(keeper)
zoo.add_staff(veterinarian)

animal_sound(zoo.animals)

keeper.feed_animal(bird)
veterinarian.heal_animal(mammal)