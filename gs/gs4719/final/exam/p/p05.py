def p05(l1=[1, 4, 3, 2, 5, 2], x=3):
    # 檢查輸入是否合法
    if not all(0 <= num <= 200 for num in l1) or not (0 <= x <= 200):
        return "輸入數值不符合條件"

    # 取出小於 x 的元素並排序
    less_than_x = sorted([num for num in l1 if num < x])

    # 取出不小於 x 的元素
    greater_or_equal_x = [num for num in l1 if num >= x]

    # 合併兩個列表
    output_list = less_than_x + greater_or_equal_x

    return output_list

# 測試範例
print(p05([1, 4, 3, 2, 5, 2], 3))  # Example 1
print(p05([2, 1], 2))  # Example 2
