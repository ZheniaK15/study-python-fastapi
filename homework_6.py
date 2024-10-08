class Animal:
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f'{self.name}, {self.sound}')

animal_1 = Animal("Мурка", "Кішка", 7, "урчить")
animal_2 = Animal("Арчи", "Німецька вівчарка", 5, "гавкає")

animal_1.make_sound()
animal_2.make_sound()



class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        if self.width < 0 or self.height < 0:
            print("Помилка: Сторони прямокутника не можуть бути від'ємними.")
        else:
            area = self.height * self.width
            print("Площа прямокутника:", area)

Rectangle_1 = Rectangle(1, 67)
Rectangle_2 = Rectangle(-34, 1000)
Rectangle_3 = Rectangle(65, 80)

Rectangle_2.calculate_area()
Rectangle_1.calculate_area()
Rectangle_3.calculate_area()
