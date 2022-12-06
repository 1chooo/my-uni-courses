import random

arr = []

for i in range(0, 6) :
    temp = random.randint(1, 49)
    arr.append(temp)

arr = sorted(arr)

print(arr)