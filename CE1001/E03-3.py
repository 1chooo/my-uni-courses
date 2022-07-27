# -*- coding: utf-8 -*-

list1 = "0123456789" +\
       "ABCDEFGHIJKLMNOPQRSTUVWXYZ" +\
       "abcdefghijklmnopqrstuvwxyz"         # 0 ~ 9, 10 ~ 35, 36 ~ 61
list1 = list(list1)

while True:
    r = input()
    if r == "-1":
        break

    rLength = len(r)
    sum = 0
    for i in range(rLength):
        a = list1.index(r[i])
        sum += a

    aMax = list1.index(r[rLength-1])

    for i in range(aMax, 63):
        if sum % i == 0:
            print(i + 1)
            break
        elif i == 62:
            print("such number is impossible!")