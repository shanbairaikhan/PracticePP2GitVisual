class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Rayhan", 18)
print(p.name, p.age)


class Animal:
    def speak(self):
        print("I make sounds!")

a = Animal()
a.speak()


class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(3)
print(c.area())


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

r = Rectangle(2, 5)
print(r.area())


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        return sum(self.marks) / len(self.marks)

s = Student("Ali", [70, 80, 90])
print(s.average())


class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Woof!")

d = Dog("Buddy")
d.speak()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1.x, p1.y, p2.x, p2.y)


class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def info(self):
        return f"{self.brand}, {self.year}"

car = Car("Honda", 2022)
print(car.info())
