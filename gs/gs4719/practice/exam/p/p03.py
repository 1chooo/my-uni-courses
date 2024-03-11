def p03(x=123):
    reverse=None
    # ↓程式區域↓
    # 將數字轉換為字串，然後反轉字串，最後再轉回整數
    if x >= 0:
        reverse = int(str(x)[::-1])
    else:
        reverse = -int(str(-x)[::-1])

    # ↑程式區域↑
    return reverse

# 測試程式碼
if __name__ == "__main__":
    result = p03(123)
    print(result)
