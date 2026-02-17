class Person:
    def __init__(self, name):
        self.name = name

p = Person("Rayhan")
print(p.name)


class Employee:
    def __init__(self, name, salary=1000):
        self.name = name
        self.salary = salary

e = Employee("Ali")
print(e.salary)


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

d = Dog("Max", "Beagle")
print(d.name, d.breed)


class Cat:
    def __init__(self, name, color="White"):
        self.name = name
        self.color = color

c = Cat("Luna")
print(c.name, c.color)


class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

car = Car("Toyota", 2021)
print(car.brand, car.year)


class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

l = Laptop("HP", 16)
print(l.brand, l.ram)


class Phone:
    def __init__(self, brand, storage=64):
        self.brand = brand
        self.storage = storage

ph = Phone("Xiaomi")
print(ph.brand, ph.storage)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

b = Book("Python 101", "John Doe")
print(b.title, b.author)
