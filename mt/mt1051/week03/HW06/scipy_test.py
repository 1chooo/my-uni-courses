# -*- coding: utf-8 -*-
"""
Date: 2023/09/25
HW: 06
Author: 林群賀
Student Number: 109601003
"""

import numpy as np
from scipy.stats import norm

u = 2.64
a = 0.38

x_values = [
    0.5, 1.5, 2.5, 
    3.5, 4.5, 5.5, 
    6.5,
]

pdf_values = [norm.pdf(x, loc=u, scale=a) for x in x_values]

for x, pdf in zip(x_values, pdf_values):
    print(f'x = {x}: PDF = {pdf}')
