class Animal:
    def speak(self):
        print("Animal sound")
class Cat(Animal):
    pass
c = Cat()
c.speak()


class Person:
    def greet(self):
        print("Hello")
class Student(Person):
    def study(self):
        print("Studying")
s = Student()
s.greet()
s.study()


class Vehicle:
    def start(self):
        print("Vehicle starting")
class Car(Vehicle):
    def start(self):
        print("Car starting")
v = Car()
v.start()


class Shape:
    def __init__(self, color):
        self.color = color
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
c = Circle("red", 5)
print(c.color, c.radius)


class Worker:
    def work(self):
        print("Working")
class Programmer(Worker):
    def code(self):
        print("Coding")
p = Programmer()
p.work()
p.code()


class Fruit:
    def taste(self):
        print("Fruit tastes good")
class Apple(Fruit):
    def taste(self):
        print("Apple is sweet")
a = Apple()
a.taste()


class BankAccount:
    def __init__(self, balance):
        self.balance = balance
class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
acc = SavingsAccount(100)
acc.deposit(50)
print(acc.balance)


class Parent:
    def hello(self):
        print("Hello from Parent")
class Child(Parent):
    def hello(self):
        super().hello()
        print("Hello from Child")
ch = Child()
ch.hello()


class Phone:
    def call(self):
        print("Calling")
class SmartPhone(Phone):
    def browse(self):
        print("Browsing")
sp = SmartPhone()
sp.call()
sp.browse()
