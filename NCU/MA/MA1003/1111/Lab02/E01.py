import random

arr = []

for i in range(0, 6) :
    temp = random.randint(1, 39)
    arr.append(temp)

arr = sorted(arr)

for i in range(0, 6) : 
    print(arr[i], end = " ")

print("特別號: ", random.randint(1, 8))