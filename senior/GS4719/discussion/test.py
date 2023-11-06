a = [1, 2, 3]
b = a

print("a:", a)
print("b:", b)

a[0] = 5

print("a:", a)
print("b:", b)

test_set = {1, 2, 3, 4, 5}
print(test_set)
print(test_set[1, 3])

import itertools

some_data = [1, 2, 4, 1, 6, 23, 3, 56, 6, 2, 3, 5, 6, 32, 2, 12, 5, 3, 2]
big_set = set(some_data)
small_set = set(itertools.islice(big_set, 5))

print(small_set)