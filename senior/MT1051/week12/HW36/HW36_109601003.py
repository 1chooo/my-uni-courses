# -*- coding: utf-8 -*-
"""
Date: 2023/12/11
HW: 36
Author: 林群賀
Student Number: 109601003
"""

import matplotlib.pyplot as plt

A = [0, 11, 23, 34, 43, 25, 26, 47, 48, 59]

plt.plot(A, lw=3)
plt.axis([0, 10, 0, 101])

plt.tick_params(axis='both', labelsize=14, color='red')
plt.title("The Chart of Exercise", fontsize=14)
plt.xlabel("X-Value", fontsize=10)
plt.xlabel("Y-Value", fontsize=10)
plt.grid()

plt.show()
