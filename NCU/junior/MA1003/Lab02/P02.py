import random

balls = ["黑", "白", "紅", "黃", "藍"]

for i in range(0, 5) :
    ball = random.choice(balls)
    print(ball, end = " ")

print()

for i in range(0, 5) :
    print(random.choice(balls), end = " ")