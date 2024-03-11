# -*- coding: utf-8 -*-
"""
Date: 2023/10/23
HW: 15
Author: 林群賀
Student Number: 109601003
"""

chicken = 0
rabbit = 0

iteration = 0
find = False

for chicken in range(1, 10):
    for rabbit in range(1, 10):
        legs = chicken * 2 + rabbit * 4
        num = chicken + rabbit

        iteration += 1

        if (legs == 30 and num == 9):
            find = True
            break
            
    if find:
        print("Chicken: ", chicken)
        print("Rabbit: ", rabbit)
        print("Iteration: ", iteration)
        break

find = False

for chicken in range(1, 10):
    rabbit = 9 - chicken  # 因為雞兔總數是9，所以兔子數量等於9減去雞的數量
    legs = chicken * 2 + rabbit * 4

    if (legs == 30 and rabbit > 0):
        find = True
        break

if find:
    print("Chicken: ", chicken)
    print("Rabbit: ", rabbit)
else:
    print("No solution found.")
