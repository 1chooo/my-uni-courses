# -*- coding: utf-8 -*-

from random import *
import matplotlib.pyplot as plt

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
b = []

for i in range(10000) :

    bl = 0
    br = 0

    for r in range(10) :

        k = randint(0, 1)

        if(k == 0) :

            bl = bl + 1
        elif(k == 1) :

            br = br + 1

    ba = br
    b.append(ba)
            



plt.hist(b, bins = a, color = (0, 0, 1))
plt.show()
