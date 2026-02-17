def first_last(*words):
    print(words[0], words[-1])

first_last("red", "green", "blue")


def repeat(msg, *names):
    for n in names:
        print(msg, n)

repeat("Welcome", "Ali", "Dana", "Nurlan")


def average(*nums):
    print(sum(nums) / len(nums))

average(2, 4, 6, 8)


def show(**person):
    print(person["city"])

show(name="Rayhan", city="Almaty")


def calc(a, b, *extra):
    print(a + b + sum(extra))

calc(1, 2, 3, 4, 5)


def product(*nums):
    p = 1
    for n in nums:
        p *= n
    print(p)

product(2, 3, 4)


def profile(**data):
    for k, v in data.items():
        print(k, v)

profile(name="Dana", age=19, uni="KBTU")


def mix(word, *nums, **info):
    print(word)
    print(nums)
    print(info)

mix("Data", 1, 2, 3, type="int", size=3)
