# -*- coding: utf-8 -*-
"""
Date: 2023/09/25
HW: 05
Author: 林群賀
Student Number: 109601003
"""

import math

def calculate_probability(x, lambda_value) -> float:
    e_to_the_minus_lambda = math.exp(-lambda_value)
    
    lambda_power_x = lambda_value ** x
    
    factorial_x = math.factorial(x)
    
    probability = (e_to_the_minus_lambda * lambda_power_x) / factorial_x
    
    return probability

def main() -> None:
    lambda_value = 0.26

    for x in range(1, 7):
        probability = calculate_probability(x, lambda_value)
        print(f'P(x={x}, lambda={lambda_value}) = {probability:.6f}')

if __name__ == '__main__':
    main()
