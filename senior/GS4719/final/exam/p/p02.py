def p02(a=1, b=100):
    evensum = 0
    # ↓程式區域↓
    # 確保 a 是偶數，如果不是偶數，則將其增加 1
    if a % 2 != 0:
        a += 1

    for num in range(a, b + 1, 2):  # 從 a 開始遍歷到 b，步長為 2
        evensum += num  # 將偶數加到總和中

    # ↑程式區域↑
    return evensum

print(p02(1, 100))