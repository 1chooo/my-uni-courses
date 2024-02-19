# -*- coding: utf-8 -*-
"""
Date: 2023/09/25
HW: 01
Author: 林群賀
Student Number: 109601003
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x)
def f(x):
    if x == 0:
        return 0  # Avoid division by zero
    return np.sin(x) / (2 * np.abs(x))

# Generate x values in the range of -10 * pi to 10 * pi
x = np.linspace(-10 * np.pi, 10 * np.pi, 1000)

# Calculate corresponding y values
y = [f(xi) for xi in x]

# Create a plot to visualize the function
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='f(x) = sin(x) / abs(2 * x)')
plt.title('f(x) = sin(x) / abs(2 * x)')
plt.xlabel('x')
plt.ylabel('Y')
plt.grid(True)
plt.legend()
plt.show()
