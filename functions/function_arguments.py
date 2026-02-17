# 1
def square(x):
    return x * x

print(square(4))


# 2
def greet(name="Guest"):
    print("Hello,", name)

greet()
greet("Rayhan")


# 3
def add(a, b):
    print(a + b)

add(3, 5)


# 4
def total(*numbers):
    s = 0
    for n in numbers:
        s += n
    print(s)

total(1, 2, 3)
total(10, 20, 30, 40)


# 5
def info(**data):
    print(data)

info(name="Rayhan", age=18)
