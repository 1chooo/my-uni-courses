import random

inNum = int(input())

arr = []

for i in range(1, inNum + 1) :
    temp = random.randint(1, 9)
    print(temp, "|", temp * "*")
