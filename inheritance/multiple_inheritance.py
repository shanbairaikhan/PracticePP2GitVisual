class A:
    def method_a(self):
        print("Method A")
class B:
    def method_b(self):
        print("Method B")
class C(A, B):
    pass
c = C()
c.method_a()
c.method_b()


class Parent1:
    def greet1(self):
        print("Hello Parent1")
class Parent2:
    def greet2(self):
        print("Hello Parent2")
class Child(Parent1, Parent2):
    pass
ch = Child()
ch.greet1()
ch.greet2()


class X:
    def fx(self):
        print("X function")
class Y:
    def fy(self):
        print("Y function")
class Z(X, Y):
    def fz(self):
        print("Z function")
z = Z()
z.fx()
z.fy()
z.fz()

class Animal:
    def eat(self):
        print("Animal eats")
class Bird:
    def fly(self):
        print("Bird flies")
class Parrot(Animal, Bird):
    def speak(self):
        print("Parrot talks")
p = Parrot()
p.eat()
p.fly()
p.speak()


class Teacher:
    def teach(self):
        print("Teaching")
class Musician:
    def play(self):
        print("Playing music")
class MultiTalented(Teacher, Musician):
    pass
mt = MultiTalented()
mt.teach()
mt.play()


class Vehicle:
    def wheels(self):
        print("Has wheels")
class Engine:
    def start(self):
        print("Engine starts")
class Truck(Vehicle, Engine):
    pass
t = Truck()
t.wheels()
t.start()


class Father:
    def skills(self):
        print("Father skills")
class Mother:
    def skills(self):
        print("Mother skills")
class Son(Father, Mother):
    pass
s = Son()
s.skills()


class Phone:
    def call(self):
        print("Calling")
class GPS:
    def navigate(self):
        print("Navigating")
class SmartDevice(Phone, GPS):
    pass
sd = SmartDevice()
sd.call()
sd.navigate()


class Writer:
    def write(self):
        print("Writing")
class Photographer:
    def take_photo(self):
        print("Taking photo")
class Creator(Writer, Photographer):
    pass
cr = Creator()
cr.write()
cr.take_photo()


class Engine:
    def start(self):
        print("Engine starts")
class Wheels:
    def roll(self):
        print("Wheels roll")
class Scooter(Engine, Wheels):
    def drive(self):
        print("Scooter drives")
sc = Scooter()
sc.start()
sc.roll()
sc.drive()
