# -*- coding: utf-8 -*-
"""
Date: 2023/11/06
Question: 05
Author: 林群賀
Student Number: 109601003
"""

import math

def supply_price(P):
    return (
        0.18 * 
        math.exp(math.sqrt(0.2 * P)) -
        255.3
    )

def demand_price(P):
    return (
        -(0.35 * P) + 
        563.5
    )

def main() -> None:

    price = 0
    tolerance = 0.001

    while True:
        Qs = supply_price(price)
        Qs = round(Qs, 3)
        Qd = demand_price(price)
        Qd = round(Qd, 3)

        if abs(Qs - Qd) < tolerance:
            print(f"價格 (P) = {price:.3f}")
            print(f"均衡供應數量 (Qs) = {Qs:.3f}")
            print(f"均衡需求數量 (Qd) = {Qd:.3f}")
            break

        price += 0.0001

if __name__ == "__main__":
    main()
