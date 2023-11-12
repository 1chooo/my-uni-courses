# -*- coding: utf-8 -*-
"""
Date: 2023/11/06
Question: 04
Author: 林群賀
Student Number: 109601003
"""

listA = [256, 41, 23, 159, 98]
listB = [53, 86, 512, 346, 66, 39]

listA.reverse()
print("(1). 反轉次序的 listA:", listA)

del listB[2]
listB.insert(4, 93)
print("(2). 修改後的 listB:", listB)

listC = listA + listB
print("(3). 將 listB 連接到 listA 之後的 listC:", listC)

listC.sort()
print("(4). 由小到大排序後的 listC:", listC)

total_sum = sum(listC)
print("(5). listC 所有元素的總和:", total_sum)
