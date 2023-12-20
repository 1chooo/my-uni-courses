# -*- coding: utf-8 -*-
"""
Date: 2023/12/18
HW: 42
Author: 林群賀
Student Number: 109601003
"""

import matplotlib.pyplot as plt
import math

# 請設計一個程式， x 介於 -5, 11，繪製函數圖形

# f(x) = 1/ (delta * sqrt(2 * pi)) * exp(-1/2 * ((x - mu) / delta) ** 2)

# mu = 3.0, delta = 2.0

import matplotlib.pyplot as plt
import numpy as np

# 定義函數
def gaussian_function(x, mu, delta):
    return 1 / (delta * np.sqrt(2 * np.pi)) * np.exp(-1/2 * ((x - mu) / delta) ** 2)

# 設定 mu 和 delta 的值
mu_value = 3.0
delta_value = 2.0

# 生成 x 值範圍
x_values = np.linspace(-5, 11, 1000)  # 調整需要的 x 範圍和精度

# 計算對應的 y 值
y_values = gaussian_function(x_values, mu_value, delta_value)

# 繪製圖形
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='f(x) = 1/(δ√(2π)) * exp(-1/2 * ((x - μ) / δ)^2)')
plt.title('Gaussian Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.grid(True)
plt.tight_layout()

plt.show()
