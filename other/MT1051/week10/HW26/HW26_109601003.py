# -*- coding: utf-8 -*-
"""
Date: 2023/11/27
HW: 26
Author: 林群賀
Student Number: 109601003
"""

import numpy as np

A = np.array(
    [[25, 32, 18], 
     [16, 22, 54],
     [31, 29,  8],
     [25, 14, 65],]
)

B = np.array(
    [[14, 24,  7], 
     [52, 32, 13],
     [33, 24, 55],
     [72, 81, 29],]
)

result = A + B

print(f"A + B = \n{result}")


