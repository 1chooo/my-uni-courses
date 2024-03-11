# -*- coding: utf-8 -*-
"""
Date: 2023/11/23
HW: 24
Author: 林群賀
Student Number: 109601003
"""

def find_min(nums):
    nums = [23, 78, 45, 8, 32, 56, 14, 25, 4, 62]
    min = nums[0]
    for i in nums:
        if i < min:
            min = i
    print(f"最小值為 {min}")

def main():
    listA = [23, 78, 45, 8, 32, 56, 14, 25, 4, 62]
    find_min(listA)

if __name__ == "__main__":
    main()
