def p03(x=123):
    is_negative = x < 0  # 檢查是否為負數
    x = abs(x)  # 將數字轉換為正數，方便反轉處理

    reverse = 0
    while x != 0:
        remainder = x % 10  # 取出最後一位數字
        reverse = reverse * 10 + remainder  # 將數字反轉
        x //= 10  # 去除最後一位數字

    # 如果原始數字為負數，則返回反轉後的負數
    if is_negative:
        reverse *= -1

    return reverse

print(p03(123))
print(p03(-123))
print(p03(-120))