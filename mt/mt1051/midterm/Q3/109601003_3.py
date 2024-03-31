# -*- coding: utf-8 -*-
"""
Date: 2023/11/06
Question: 03
Author: 林群賀
Student Number: 109601003
"""

myList = [21, 0, 95, 17, 3, 19, 31, 2, 8]

for i in range(len(myList)):
    if myList[i] % 2 == 0:
        myList[i] = "even"
    else:
        myList[i] = myList[i] % 17

print(myList)
