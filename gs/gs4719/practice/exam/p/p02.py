def p02(a=1, b=100):
    evensum = None  # 初始化偶數總和為 0

    # 確保 a 是偶數，如果 a 是奇數，則將其增加 1
    if a % 2 != 0:
        a += 1

    for num in range(a, b + 1, 2):  # 從 a 開始，間隔為 2 遍歷到 b（包括 b）
        evensum += num

    return evensum

# 測試程式碼
if __name__ == "__main__":
    result = p02(1, 100)
    print(result)
