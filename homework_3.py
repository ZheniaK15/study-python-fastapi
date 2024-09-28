password = "password123"
user_password = input("Введіть пароль: ")

if user_password == password:
    print("Ви увійшли в систему")
else:
    print("Неправильний пароль")

day_number = int(input("Введіть номер дня тижня (1-7): "))

if day_number == 1:
    print("Понеділок")
elif day_number == 2:
    print("Вівторок")
elif day_number == 3:
    print("Середа")
elif day_number == 4:
    print("Четвер")
elif day_number == 5:
    print("П'ятниця")
elif day_number == 6:
    print("Субота")
elif day_number == 7:
    print("Неділя")
else:
    print("Неправильний номер дня")

number = 9
print("Таблиця множення для", number)

for a in range(1, 11):
    print(number, "*", a, "=", number * a)

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_of_numbers = 0

for d in list_of_numbers:
    sum_of_numbers += d

print("Сума чисел:", sum_of_numbers)

b = 9
factorial = 1

for a in range(1, b + 1):
    factorial *= a

print("Факторіал числа", b, "дорівнює", factorial)

a = 10
b = 30
print("Прості числа в діапазоні від", a, "до", b, ":")

for num in range(a, b + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
