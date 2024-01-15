def p01(*nums):
    if len(nums) == 0:
        return None  # 如果沒有輸入數字，返回 None

    minnum = float('inf')  # 將最小值設置為正無窮大

    for num in nums:
        if isinstance(num, (int, float)):
            minnum = min(minnum, num)

    return float(minnum)  # 返回最小值，轉換成浮點數格式

# 測試程式碼
if __name__ == "__main__":
    result = p01(5, 3, 9, 1, 7)
    print(result)
