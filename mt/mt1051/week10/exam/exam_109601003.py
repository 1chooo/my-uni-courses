# -*- coding: utf-8 -*-
"""
Date: 2023/11/27
HW: exam
Author: 林群賀
Student Number: 109601003
"""

def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] >= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1

def quickselect(nums, low, high, k):
    if low <= high:
        pivot_index = partition(nums, low, high)

        if pivot_index == k:
            return nums[pivot_index]
        elif pivot_index < k:
            return quickselect(nums, pivot_index + 1, high, k)
        else:
            return quickselect(nums, low, pivot_index - 1, k)

def find_kth_largest(nums, k):
    return quickselect(nums, 0, len(nums) - 1, k - 1)

# Given list of numbers
numbers = [39, 82, 12, 54, 34, 23, 52, 19, 53, 55, 73, 71, 62, 11]
k = 5  # Find the 5th largest number

result = find_kth_largest(numbers, k)
print(f"The {k}th largest number is: {result}")


