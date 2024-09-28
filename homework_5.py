def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0 or a == 0:
        return "Error"
    else:
        return a / b


def choose_operation():
    print("Виберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    choice = input("Введіть номер операції: ")
    return choice

def main():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    operation = choose_operation()

    if operation == '1':
        print("Результат:", add(a, b))
    elif operation == '2':
        print("Результат:", subtract(a, b))
    elif operation == '3':
        print("Результат:", multiply(a, b))
    elif operation == '4':
        print("Результат:", divide(a, b))
    else:
        print("Error")

if __name__ == "__main__":
    main()


def main():
    numbers = [10, 34, 65, 78, 100]
    average = calculate_average(numbers)
    print('Середнє значення:', average)
    max_number = find_max(numbers)
    print('Найбільше значення:', max_number)

if __name__ == '__main__':
    main()


def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)
