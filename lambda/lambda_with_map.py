nums = [1, 2, 3, 4]
for x in map(lambda n: n*2, nums):
    print(x)

words = ["hi", "python", "code"]
for w in map(lambda s: s.upper(), words):
    print(w)

nums = [5, 10, 15]
for n in map(lambda n: n + 5, nums):
    print(n)

nums = [1, 2, 3, 4]
print(list(map(lambda n: n*2, nums)))

words = ["hi", "python", "code"]
print(list(map(lambda s: s.upper(), words)))

nums = [5, 10, 15]
print(list(map(lambda n: n + 5, nums)))
