# -*- coding: utf-8 -*-
"""
Date: 2023/09/25
HW: 06
Author: 林群賀
Student Number: 109601003
"""

import math

def normal_distribution(x, mu, a) -> float:
    coefficient = 1 / (a * math.sqrt(2 * math.pi))
    exponent = -0.5 * ((x - mu) / a) ** 2

    return coefficient * math.exp(exponent)

def main() -> None:
    mu = 2.64
    a = 0.38

    x_values = [
        0.5, 1.5, 2.5, 
        3.5, 4.5, 5.5, 
        6.5,
    ]

    for x in x_values:
        pdf = normal_distribution(x, mu, a)
        print(f'x = {x}: Normal Distribution = {pdf}')

if __name__ == '__main__':
    main()
