import random

arr = []

for i in range(0, 50) :
    temp = random.randint(1, 6)
    arr.append(temp)

# count = []
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0

for i in range(0, 50) :
    if arr[i] == 1 :
        count1 += 1
    elif arr[i] == 2 :
        count2 += 1
    elif arr[i] == 3 :
        count3 += 1
    elif arr[i] == 4 :
        count4 += 1
    elif arr[i] == 5 :
        count5 += 1
    else :
        count6 += 1

print(1, "->", count1)
print(2, "->", count2)
print(3, "->", count3)
print(4, "->", count4)
print(5, "->", count5)
print(6, "->", count6)

print("max =", max(count1, count2, count3, count4, count5, count6))


count = [0, 0, 0, 0, 0 ,0]

for i in range(0, 50) :
    temp = random.randint(0, 5)
    count[temp] += 1

print(count)