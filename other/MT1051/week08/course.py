# -*- coding: utf-8 -*-
"""
Date: 2023/11/13
HW: 20
Author: 林群賀
Student Number: 109601003
"""

list_a = [9, 18, 12, 8, 34, 20, 52, 10, 32, 5, 73, 47]

count = 0

for i in range(len(list_a)):
    if list_a[i] > 15:
        count += 1

print(f"大於 15 的數共有 {count} 個")


set_a = {"國文", "英文", "歷史", "地理", "數學"}
set_b = {"數學", "物理", "化學", "國文"}

set_intersection = set_a & set_b
set_union = set_a | set_b
set_difference = set_a - set_b
set_symmetric_difference = set_a ^ set_b

print(f"交集: {set_intersection}")
print(f"聯集: {set_union}")
print(f"差集: {set_difference}")
print(f"對稱差集: {set_symmetric_difference}")


tuple_a = (3, 6, 1, 2, 7)
