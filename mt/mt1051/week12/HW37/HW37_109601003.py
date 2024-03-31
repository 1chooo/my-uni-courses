# -*- coding: utf-8 -*-
"""
Date: 2023/12/11
HW: 37
Author: 林群賀
Student Number: 109601003
"""

import matplotlib.pyplot as plt

A = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
B = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

plt.plot(A, lw=3)
plt.plot(B, lw=3)
plt.axis([0, 10, 0, 101])

plt.tick_params(axis='both', labelsize=14, color='red')
plt.title("The Chart of Exercise", fontsize=14)
plt.xlabel("X-Value", fontsize=10)
plt.xlabel("Y-Value", fontsize=10)
plt.grid()

plt.show()
