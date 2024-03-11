# -*- coding: utf-8 -*-
"""
Date: 2023/12/25
Question: 01
Author: 林群賀
Student Number: 109601003
有用 ChatGPT
"""

import numpy as np

seasons = [
    "Q1",
    "Q2",
    "Q3",
    "Q4"    
]

product_names = [
    "USB 充電線",
    "手機殼",
    "耳機",
]

product_prices = [
    5,
    10,
    20
]

product_sales = np.array([
    [1000, 500, 200],
    [1500, 800, 300],
    [2000, 1200, 400],
    [2500, 1500, 500]
])

# 計算營收
revenues = product_sales * np.array(product_prices)

# 輸出營收矩陣
print("Q1:")
print(revenues)

print("Q2:")

# 將產品價格轉換成與產品銷售數量相同形狀的二維 NumPy 數組
prices_array = np.array(product_prices)
prices_matrix = np.tile(prices_array, (len(seasons), 1))

# 計算每個產品的總營收
total_revenues_per_product = np.sum(product_sales * prices_matrix, axis=0)

# # 輸出每個產品的總營收
# for i, product in enumerate(product_names):
#     print(f"{product}的總營收: {total_revenues_per_product[i]}")

print(total_revenues_per_product)


print("Q3:")

# 計算每個季度所有產品的總營收
total_revenues_per_quarter = np.sum(revenues, axis=1)

# # 輸出每個季度所有產品的總營收
# for i, quarter in enumerate(seasons):
#     print(f"{quarter}: {total_revenues_per_quarter[i]}")

print(total_revenues_per_quarter)
print("Q4:")

max_values = np.max(revenues.T, axis=1)

max_value = np.max(max_values)
max_value_index = np.where(revenues == max_value)

# print(max_value_index)

print(f"第 {max_value_index[1][0] + 1} 個產品在第 {max_value_index[0][0]} 季度有最高之營收")
