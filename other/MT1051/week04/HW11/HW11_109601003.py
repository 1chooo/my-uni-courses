# -*- coding: utf-8 -*-
"""
Date: 2023/10/02
HW: 11
Author: 林群賀
Student Number: 109601003
"""

from typing import Any


class MultiplicationTable:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def __init__(self) -> None:
        pass

    def generate_table(self):
        for j in range(1, 10):
            for i in range(2, 10):
                tmp = i * j
                print(f"{i}x{j}", end="")
                if tmp >= 10:
                    print("=", end="")
                else:
                    print("= ", end="")
                if i == 9:
                    print(i * j)
                else:
                    print(i * j, end=" ")

def main() -> None:
    table = MultiplicationTable()
    table.generate_table()

if __name__ == "__main__":
    main()
