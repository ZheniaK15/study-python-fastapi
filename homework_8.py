class User:
    def __init__(self):
        self.__name = ""
        self.__email = ""
        self.__password = ""

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password


user = User()
user.set_name("Alian Ford")
user.set_email("alian201935@gmail.com")
user.set_password("Alian-3523")
print("Ім'я користувача:", user.get_name())
print("Електронна пошта:", user.get_email())
print("Пароль:", user.get_password())

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


circle = Circle(5)
rectangle = Rectangle(9, 3)
triangle = Triangle(6, 2)
print("Площа кола:", circle.calculate_area())
print("Площа прямокутника:", rectangle.calculate_area())
print("Площа трикутника:", triangle.calculate_area())
