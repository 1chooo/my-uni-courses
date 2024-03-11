# -*- coding: utf-8 -*-
"""
Date: 2023/10/02
HW: 09
Author: 林群賀
Student Number: 109601003
"""

from typing import Any


class FunctionCalculator:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def __init__(self) -> None:
        pass

    def f(self, x) -> float:
        return 4.6 * x * x - 6.5 * x + 13.4

    def calculate_and_print(self, start, end) -> None:
        for i in range(start, end + 1):
            x = i + 0.4
            result = self.f(x)
            print(f'f({x}) = {result}')

def main() -> None:
    calculator = FunctionCalculator()
    calculator.calculate_and_print(9, 20)

if __name__ == '__main__':
    main()
