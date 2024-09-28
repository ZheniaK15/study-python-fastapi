a = [1, 2, 3, 4, 5]
a.append(10)
a.append(20)
a.remove(10)
print(a)


b = a[0] + a[1] + a[2] + a[3] + a[4]
print(b)

a = [1, 2, 3, 4, 5]
b = [number * 2 for number in a]
print(b)

a = ('apple', 'banana', 'orange')
print(a[0])
print(a[1])
print(a[2])

a = ('apple', 'banana', 'orange')
b = (1, 2, 3)
c = a + b
print(c)

list = {'name': 'Jon', 'age': 21, 'country': 'USA', 'sport': 'football'}
for key, value in list.items():
    print(f"{key}: {value}")

books = {
    'Майстер і Маргарита': 1967,
    'Маленький принц': 1943,
    'Гаррі Поттер і філософський камінь': 1997,
}

copy_books = books.copy()
dict_update = {'Гаррі Поттер та Таємна кімната': 1998}
books.update(dict_update)
print(books)

countries_capitals = {
    'Україна': 'Київ',
    'Польща': 'Варшава',
    'Німеччина': 'Берлін',
    'Словаччина': 'Братислава',
}

country = input("Введіть назву країни: ")
capital = countries_capitals.get(country)

if capital:
    print(f"Столиця країни {country}: {capital}")
else:
    print(f"Країни {country} немає у базі даних.")
