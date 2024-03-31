# -*- coding: utf-8 -*-
"""
Date: 2023/10/02
HW: 10
Author: 林群賀
Student Number: 109601003
"""

# N = int(input())

# R = 0

# for i in range(2, N + 1):
#     R += (1 - 1 / i)

# print(R)

class CalculateR:
    def __init__(self, N):
        self.N = N

    def calculate(self):
        R = 0
        for i in range(2, self.N + 1):
            R += (1 - 1 / i)
        return R

if __name__ == '__main__':
    N = int(input("Enter a value for N: "))
    calculator = CalculateR(N)
    result = calculator.calculate()
    print(result)
