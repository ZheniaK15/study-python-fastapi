class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def create_user(self):
        return (self.name, self.email)

    def update_email(self, new_email):
        self.email = new_email

    def delete_user(self):
        print(f"Користувач {self.name} був видалений.")


user1 = User("Ivan Kurapov", "IvanKurapov2146@example.com")
print("Поточна електронна пошта:", user1.email)
user1.update_email("Ivan3557@example.com")
print("Нова електронна пошта:", user1.email)
user1.delete_user()

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Calculator_of_area:
    @staticmethod
    def calculate_area(shape):
        return shape.calculate_area()

circle = Circle(9)
rectangle = Rectangle(4, 2)
print("Площа кола:", Calculator_of_area.calculate_area(circle))
print("Площа прямокутника:", Calculator_of_area.calculate_area(rectangle))

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

def print_area(shape):
    print("Area:", shape.calculate_area())

rectangle = Rectangle(8, 4)
circle = Circle(5)
print_area(rectangle)
print_area(circle)

class NetworkPrinterPrint(ABC):
    @abstractmethod
    def print_document(self):
        pass

class NetworkPrinterScan(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class NetworkPrinterCopy(ABC):
    @abstractmethod
    def copy_document(self):
        pass

class Printer(NetworkPrinterPrint):
    def print_document(self):
        print('Document is printing..........')

class Scanner(NetworkPrinterScan):
    def scan_document(self):
        print('Document is scanning..........')

document1 = Printer()
document2 = Scanner()
document1.print_document()
document2.scan_document()

class NetworkPrinter(ABC):
    @abstractmethod
    def print_document(self):
        pass

    @abstractmethod
    def scan_document(self):
        pass

    @abstractmethod
    def copy_document(self):
        pass

class Printer:
    def __init__(self, network_printer: NetworkPrinter):
        self.network_printer = network_printer

    def print_document(self):
        self.network_printer.print_document()

class Scanner:
    def __init__(self, network_printer: NetworkPrinter):
        self.network_printer = network_printer

    def scan_document(self):
        self.network_printer.scan_document()

class PrinterScanner:
    def __init__(self, network_printer: NetworkPrinter):
        self.network_printer = network_printer

    def print_document(self):
        self.network_printer.print_document()

    def scan_document(self):
        self.network_printer.scan_document()
