# -*- coding: utf-8 -*-
"""
Date: 2023/12/25
Question: 03
Author: 林群賀
Student Number: 109601003
有用 ChatGPT
"""

import numpy as np

# 定義多項式的係數
coefficients = [1, -6, 11, -6]

# 求解多項式方程的根
roots = np.roots(coefficients)

# 輸出解
print("Q1:")
print(roots)


import numpy as np
import matplotlib.pyplot as plt

# 定義 x 的範圍
x = np.arange(0, 5, 0.01)

# 計算方程的值
y = x**3 - 6*x**2 + 11*x - 6

# 繪製圖形
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$x^3 - 6x^2 + 11x - 6$')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('109601003 Cubic Equation')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# 計算方程的根
roots = np.roots([1, -6, 11, -6])

# 在圖形上標記根
for root in roots:
    if root.imag == 0:  # 只有實數根才標記
        plt.scatter(root.real, 0, color='red', s=50, label='Roots')

plt.legend()
plt.grid(True)
plt.show()

