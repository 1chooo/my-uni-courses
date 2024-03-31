# -*- coding: utf-8 -*-
"""
Date: 2023/11/06
Question: 07
Author: 林群賀
Student Number: 109601003
"""

coin_denominations = [1, 5, 10]
min_coins = [1, 1, 1]
max_coins = [20, 20, 20]
target_value = 108

min_combination = None
max_combination = None
min_coin_count = float('inf')
max_coin_count = 0

for count1 in range(min_coins[0], max_coins[0] + 1):
    for count5 in range(min_coins[1], max_coins[1] + 1):
        for count10 in range(min_coins[2], max_coins[2] + 1):
            total_value = count1 * coin_denominations[0] + count5 * coin_denominations[1] + count10 * coin_denominations[2]
            
            if total_value == target_value:
                if count1 + count5 + count10 < min_coin_count:
                    min_combination = [count1, count5, count10]
                    min_coin_count = count1 + count5 + count10
                if count1 + count5 + count10 > max_coin_count:
                    max_combination = [count1, count5, count10]
                    max_coin_count = count1 + count5 + count10

print("硬幣數量最多的组合:", max_combination)
print("硬幣數量最少的组合:", min_combination)
