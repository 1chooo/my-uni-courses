def p06(nums=[2, 7, 11, 15], target=9):
    # 創建一個字典來存儲數字和它們的索引
    num_indices = {}

    # 遍歷列表中的數字
    for i, num in enumerate(nums):
        # 計算與目標值的差值
        complement = target - num

        # 檢查差值是否在字典中
        if complement in num_indices:
            # 如果在字典中找到了差值，返回兩個數字的索引
            return [num_indices[complement], i]

        # 將當前數字存入字典
        num_indices[num] = i

    # 若沒有符合條件的數字組合，返回空列表
    return []

# 測試範例
print(p06([2, 7, 11, 15], 9))  # Example 1
print(p06([3, 2, 4], 6))  # Example 2
print(p06([3, 3], 6))  # Example 3
