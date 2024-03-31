# -*- coding: utf-8 -*-
"""
Date: 2023/10/23
HW: 16
Author: 林群賀
Student Number: 109601003
"""

def supply_price(P):
    return 43.3 + 1.25 * P

def demand_price(P):
    return 96.3 - 2.13 * P

def main() -> None:

    i = 0
    tolerance = 0.0001

    while True:
        Qs = supply_price(i)
        Qs = round(Qs, 3)
        Qd = demand_price(i)
        Qd = round(Qd, 3)

        if abs(Qs - Qd) < tolerance:
            print(f"均衡价格 (P) = {i:.3f}")
            print(f"均衡数量 (Q) = {Qs:.3f}")
            break

        i += 0.0001


if __name__ == "__main__":
    main()
