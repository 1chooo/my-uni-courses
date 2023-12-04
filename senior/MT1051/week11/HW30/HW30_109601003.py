# -*- coding: utf-8 -*-
"""
Date: 2023/12/04
HW: 30
Author: 林群賀
Student Number: 109601003
"""

import numpy as np

seasons = np.array([
    "Q1",
    "Q2",
    "Q3",
    "Q4",
])
location = np.array([
    "台北 - 桃園", 
    "台北 - 新竹", 
    "台北 - 台中", 
    "台北 - 嘉義", 
    "台北 - 高雄", 
    "台北 - 花蓮",
])
prices = np.array(
    [44, 116, 241, 386, 544, 284]
)
people = np.array([
    [35273, 21534, 12573, 31567, 52386, 44138],
    [25673, 55728, 31245, 33278, 51342, 22464],
    [21345, 22179, 32189, 36296, 33106, 43278],
    [53278, 32785, 43167, 21367, 44579, 32685],
])

revenue = prices * people
# season_total = []

# for i in range(len(revenue)):
#     total = 0
#     for j in range(6):
#         total += revenue[i][j]
#     season_total.append(total)


# print(season_total)

# Calculate season_total using numpy
season_total = np.sum(revenue, axis=1)

print(season_total)
