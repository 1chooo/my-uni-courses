# -*- coding: utf-8 -*-
"""
Date: 2023/09/25
HW: 07
Author: 林群賀
Student Number: 109601003
"""

import math
from typing import Any

class ECalculator:

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def __init__(self):
        pass

    def calculate(self, num):
        if num < 50:
            num = math.sqrt(num) * 10
        else:
            num += 12
        return num

def main() -> None:
    e_calculator = ECalculator()
    num = float(input("Please input the value E: "))
    result = e_calculator.calculate(num)
    print("The final result of E:", result)

if __name__ == '__main__':
    main()
