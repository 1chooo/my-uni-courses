# -*- coding: utf-8 -*-
"""
Date: 2023/09/25
Warm up
Author: 林群賀
Student Number: 109601003
"""

import math
from typing import Any

def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (
            round(root1, 2), 
            round(root2, 2)
        )
    elif discriminant == 0:
        root1 = -b / (2 * a)
        return round(root1, 2)
    else:
        return "No real roots"

if __name__ == "__main__":
    try:
        a = float(input("Enter the value of a: "))
        b = float(input("Enter the value of b: "))
        c = float(input("Enter the value of c: "))
        
        roots = find_roots(a, b, c)
        
        if isinstance(roots, tuple):
            print(f"The roots of the equation are {roots[0]} and {roots[1]}")
        elif isinstance(roots, float):
            print(f"The root of the equation is {roots}")
        else:
            print(roots)
    except ValueError:
        print("Invalid input. Please enter valid numerical values for a, b, and c.")

class FindRoot:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def __init__(self) -> None:
        pass

    def get_parameters(self,) -> tuple:
        a = float(input("Enter the value of a: "))
        b = float(input("Enter the value of b: "))
        c = float(input("Enter the value of c: "))

        return a, b, c
    
    def get_root(self, a, b, c):
        discriminant = b ** 2 - 4 * a * c
    
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return (
                round(root1, 2), 
                round(root2, 2)
            )
        elif discriminant == 0:
            root1 = -b / (2 * a)
            return round(root1, 2)
        else:
            return "No real roots"
