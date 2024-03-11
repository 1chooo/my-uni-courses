# -*- coding: utf-8 -*-
"""
Date: 2023/12/18
HW: 41
Author: 林群賀
Student Number: 109601003
"""

import matplotlib.pyplot as plt
import math

def poisson_pmf(x, lambda_value):
    return (math.exp(-lambda_value) * (lambda_value ** x)) / math.factorial(x)

lambda_val = 1.2
x_values = list(range(0, 21))  # 調整需要的 x 範圍

pmf_values = [poisson_pmf(x, lambda_val) for x in x_values]

plt.figure(figsize=(8, 6))
plt.plot(x_values, pmf_values, marker='o', linestyle='-')
plt.title('Poisson Distribution PMF for lambda = 1.2')
plt.xlabel('x')
plt.ylabel('P(x, lambda)')

plt.grid(True)
plt.tight_layout()

plt.show()

