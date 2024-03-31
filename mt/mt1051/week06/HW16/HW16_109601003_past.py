# -*- coding: utf-8 -*-
"""
Date: 2023/10/23
HW: 16
Author: 林群賀
Student Number: 109601003
"""

def find_coin_counts(total_coins, total_value):
    for num_0_5_euro in range(0, total_coins + 1):
        for num_1_euro in range(total_coins + 1 - num_0_5_euro):
            for num_2_euro in range(total_coins + 1 - num_0_5_euro - num_1_euro):
                for num_0_2_euro in range(total_coins + 1 - num_0_5_euro - num_1_euro - num_2_euro):
                    num_0_1_euro = total_coins - num_0_5_euro - num_1_euro - num_2_euro - num_0_2_euro
                    current_value = (num_2_euro * 2 + num_1_euro + num_0_5_euro * 0.5 + num_0_2_euro * 0.2 + num_0_1_euro * 0.1)

                    if current_value == total_value and num_0_5_euro > num_1_euro and num_1_euro > num_2_euro and num_2_euro > num_0_2_euro and num_0_2_euro > num_0_1_euro:
                        return num_2_euro, num_1_euro, num_0_5_euro, num_0_2_euro, num_0_1_euro
                    
    return None

total_coins = 96
total_value = 88.8

result = find_coin_counts(total_coins, total_value)

if result:
    num_2_euro, num_1_euro, num_0_5_euro, num_0_2_euro, num_0_1_euro = result
    print(f"0.5歐元硬幣: {num_0_5_euro} 枚")
    print(f"1歐元硬幣: {num_1_euro} 枚")
    print(f"2歐元硬幣: {num_2_euro} 枚")
    print(f"0.2歐元硬幣: {num_0_2_euro} 枚")
    print(f"0.1歐元硬幣: {num_0_1_euro} 枚")
else:
    print("找不到解答")
