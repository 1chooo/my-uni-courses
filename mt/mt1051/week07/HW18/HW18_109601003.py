# -*- coding: utf-8 -*-
"""
Date: 2023/10/30
HW: 18
Author: 林群賀
Student Number: 109601003
"""

def func(y):
    return (y + 3.2) * (y - 5.3) * (y + 9.2) * (y + 2.7)

target = 1823
lower_bound = 5.3
upper_bound = 20.0
precision = 0.001

while upper_bound - lower_bound > precision:
    mid = (lower_bound + upper_bound) / 2
    if func(mid) < target:
        lower_bound = mid
    else:
        upper_bound = mid

y = (lower_bound + upper_bound) / 2

if y > 12:
    print("y is greater than 12")
elif y < 12:
    print("y is less than 12")

