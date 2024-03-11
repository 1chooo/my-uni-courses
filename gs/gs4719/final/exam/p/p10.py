def p10(n=12):
    # 建立一個長度為 n+1 的列表，初始化為最大值，用來存儲每個數字的最少完美平方數的個數
    dp = [float('inf')] * (n + 1)
    
    # 第0個數為0個完美平方數
    dp[0] = 0
    
    # 對於每個數字i，計算它的最少完美平方數的個數
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j*j] + 1)
            j += 1
    
    return dp[n]

# 測試
print(p10(12))  # 輸出：3
print(p10(13))  # 輸出：2
