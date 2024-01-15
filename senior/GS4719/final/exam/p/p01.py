def p01(*nums):
    minnum=None
    # ↓程式區域↓

    # ↑程式區域↑
    if nums:  # 確認是否有輸入數值
        minnum = min(nums)
        return float(minnum)  # 將最小值轉換為浮點數並返回
    else:
        return None  # 如果沒有輸入數值，返回None或採取其他處理方式
    return minnum