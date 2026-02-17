nums = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x > 2, nums)))

nums = [10, 15, 20, 25]
print(list(filter(lambda x: x % 5 == 0, nums)))

words = ["hi", "hello", "ok", "python"]
print(list(filter(lambda w: len(w) > 2, words)))

names = ["Ali", "Dana", "Aruzhan", "Tim"]
print(list(filter(lambda n: n.startswith("A"), names)))

nums = [-2, -1, 0, 3, 4]
print(list(filter(lambda x: x >= 0, nums)))

nums = [7, 8, 9, 10]
print(list(filter(lambda x: x % 2 == 0, nums)))

words = ["cat", "tiger", "dog", "lion"]
print(list(filter(lambda w: len(w) == 3, words)))

nums = [100, 50, 30, 200]
print(list(filter(lambda x: x < 100, nums)))
