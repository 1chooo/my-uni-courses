# -*- coding: utf-8 -*-
"""
Date: 2023/12/25
Question: 06
Author: 林群賀
Student Number: 109601003
"""

import matplotlib.pyplot as plt
import numpy as np

# 定義函數
def gaussian_function(x, mu, delta):
    return 1 / (delta * np.sqrt(2 * np.pi)) * np.exp(-1/2 * ((x - mu) / delta) ** 2)

# 設定 mu 和 delta 的值
mu_value = 0.0
delta_value = 1

# 生成 x 值範圍
x_values = np.linspace(-5, 5, 1000)  # 調整需要的 x 範圍和精度

# 計算對應的 y 值
y_values = gaussian_function(x_values, mu_value, delta_value)
y_values_2 = gaussian_function(x_values, mu_value, np.sqrt(2))

# 繪製圖形
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='$f(x) = 1/(δ√(2π)) * exp(-1/2 * ((x - μ) / δ)^2)$ (δ=1)')
plt.plot(x_values, y_values_2, label='$f(x) = 1/(δ√(2π)) * exp(-1/2 * ((x - μ) / δ)^2)$ (δ=√2))')

plt.title('Gaussian Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.grid(True)
plt.tight_layout()

plt.show()

plt.close()

delta_values = [1, np.sqrt(2)]

# 計算 f(0) 的值
f_values = [gaussian_function(0, mu_value, delta) for delta in delta_values]

# 將結果輸出到檔案
with open('109601003.txt', 'w') as file:
    file.write(f'當 δ = 1 時，f(0) = {f_values[0]}; 當 δ = √2 時，f(0) = {f_values[1]}')