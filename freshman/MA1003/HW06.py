import math

sum = 0

for i in range(7, 31):
    sum += ((math.sqrt(i - 4)) - (math.sqrt(i - 3)))

print(sum)