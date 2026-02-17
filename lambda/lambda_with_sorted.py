print(sorted([4, 1, 7, 3, 9], reverse=True))

print(sorted([4, 1, 7, 3, 9], key=lambda x: -x))

print(sorted(["dog", "cat", "elephant"]))

print(sorted(["dog", "cat", "elephant"], key=lambda x: len(x)))

print(sorted([3.5, 1.2, 4.8, 2.1], key=lambda x: int(x)))

print(sorted([(2, 3), (1, 4), (3, 1)], key=lambda x: x[1]))

print(sorted([10, -2, 5, -7], key=lambda x: abs(x)))

print(sorted(["apple", "banana", "kiwi"], key=lambda x: x.count("i")))

print(sorted([2.3, 1.5, 3.7, 0.9], key=lambda x: round(x)))
