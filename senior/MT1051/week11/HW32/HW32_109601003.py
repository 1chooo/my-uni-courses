# -*- coding: utf-8 -*-
"""
Date: 2023/12/04
HW: 31
Author: 林群賀
Student Number: 109601003
"""

import numpy as np

print("x^2 - 12x + 3 = 0")
# 方程式的係數
a = 2
b = -12
c = 3

# 計算判別式
discriminant = b**2 - 4*a*c

# 計算根
if discriminant > 0:
    # 有兩個實根
    root1 = (-b + np.sqrt(discriminant)) / (2*a)
    root2 = (-b - np.sqrt(discriminant)) / (2*a)
    print("兩個實根：")
    print(f"根1 = {root1}, 根2 = {root2}")
elif discriminant == 0:
    # 有一個重根
    root = -b / (2*a)
    print("一個重根：")
    print(f"根 = {root}")
else:
    # 虛數根
    real_part = -b / (2*a)
    imaginary_part = np.sqrt(abs(discriminant)) / (2*a)
    print("兩個虛數根：")
    print(f"根1 = {real_part} + {imaginary_part}i, 根2 = {real_part} - {imaginary_part}i")


print("-1/3x^2 + 4/9x - 4/27 = 0")
# 方程式的係數
a = float(- 1 / 3)
b = float(4 / 9)
c = float(-4 / 27)

# 計算判別式
discriminant = b**2 - 4*a*c

# 計算根
if discriminant > 0:
    # 有兩個實根
    root1 = (-b + np.sqrt(discriminant)) / (2*a)
    root2 = (-b - np.sqrt(discriminant)) / (2*a)
    print("兩個實根：")
    print(f"根1 = {root1}, 根2 = {root2}")
elif discriminant == 0:
    # 有一個重根
    root = -b / (2*a)
    print("一個重根：")
    print(f"根 = {root}")
else:
    # 虛數根
    real_part = -b / (2*a)
    imaginary_part = np.sqrt(abs(discriminant)) / (2*a)
    print("兩個虛數根：")
    print(f"根1 = {real_part} + {imaginary_part}i, 根2 = {real_part} - {imaginary_part}i")
