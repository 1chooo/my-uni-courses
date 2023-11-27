# -*- coding: utf-8 -*-
"""
Date: 2023/11/13
HW: 21
Author: 林群賀
Student Number: 109601003
"""

location = ["台北 - 桃園", "台北 - 新竹", "台北 - 台中", "台北 - 嘉義", "台北 - 高雄", "台北 - 花蓮"]
prices = [44, 116, 241, 386, 544, 284]
people = [
    [35273, 21543, 12573, 31567, 52386, 44138],
    [25673, 55728, 31245, 33278, 51342, 22464],
    [21345, 22179, 32189, 36296, 33106, 43278],
    [53278, 32785, 43167, 21367, 44579, 32685],
]

# 初始化 revenue 為二維列表
revenue = [[0] * len(people) for _ in range(len(location))]

for i in range(len(location)):
    for j in range(len(people)):
        revenue[i][j] = prices[i] * people[j][i]

print("revenue:", revenue)

for i in range(len(location)):
    print(f"{location[i]} 路線在 Q1 - Q4 的營收分別為 {revenue[i]} 元")


