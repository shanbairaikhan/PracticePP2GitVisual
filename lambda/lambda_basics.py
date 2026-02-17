sub = lambda a, b: a - b
print(sub(10, 3))


triple = lambda x: x * 3
print(triple(7))


to_lower = lambda s: s.lower()
print(to_lower("PYTHON"))


sum_first_two = lambda lst: lst[0] + lst[1]
print(sum_first_two([2, 8]))


nums = [3, 14, 9, 22]
print(list(filter(lambda x: x % 2 == 0, nums)))


last = lambda lst: lst[-1]
print(last([5, 15, 25]))


div_by_3 = lambda x: x % 3 == 0
print(div_by_3(21))


cube = lambda x: x ** 3
print(cube(4))


repeat = lambda s: s + s
print(repeat("hi"))


size = lambda s: len(s)
print(size("coding"))
