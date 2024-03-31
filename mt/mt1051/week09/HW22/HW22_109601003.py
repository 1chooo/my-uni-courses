# -*- coding: utf-8 -*-
"""
Date: 2023/11/20
HW: 22
Author: 林群賀
Student Number: 109601003
"""

def f(x):
    return 6.5 * x**2 - 7.3 * x + 2.7

for i in range(11, 21):
    num = i + 0.5
    print(f"x = {num}, f(x) = {f(num):.2f}")

