# -*- coding: utf-8 -*-
"""
Date: 2023/11/06
Question: 06
Author: 林群賀
Student Number: 109601003
"""

import math

while True:
    n = int(input("請輸入 n: "))
    k = int(input("請輸入 k: "))

    if n < k:
        print("請再輸入一次")
        continue
    elif n < 0 or k < 0:
        print("請再輸入一次")
        continue

    up = math.factorial(n)
    down = math.factorial(n - k)

    print(f"P(n, k) = {up / down}")
