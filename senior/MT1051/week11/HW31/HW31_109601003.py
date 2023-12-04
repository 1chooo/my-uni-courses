# -*- coding: utf-8 -*-
"""
Date: 2023/12/04
HW: 31
Author: 林群賀
Student Number: 109601003
"""

import numpy as np

# Coefficients of the equations
coefficients = np.array([[1, 4], [5, -1]])
constants = np.array([-1, 16])

# Solve the linear equations
solution = np.linalg.solve(coefficients, constants)

print("Solution: X =", solution[0], ", Y =", solution[1])


