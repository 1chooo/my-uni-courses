# -*- coding: utf-8 -*-
"""
Date: 2023/12/04
HW: 33
Author: 林群賀
Student Number: 109601003
"""

import numpy as np

# 2x+3y-4z+w=15
# 1x-2y+3z+w=-3
# 3x+5y+1z+w=20
# 4x+1y-1z+w=5

import numpy as np

# Coefficients matrix
coefficients = np.array([
    [2, 3, -4, 1],
    [1, -2, 3, -2],
    [3, 5, 1, -1],
    [4, 1, -1, 1]
])

# Constants vector
constants = np.array([15, -3, 20, 5])

# Solve the system of equations
solution = np.linalg.solve(coefficients, constants)

print("Solution:")
print(f"x = {round(solution[0])}, y = {round(solution[1])}, z = {round(solution[2])}, w = {round(solution[3])}")
