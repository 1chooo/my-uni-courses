def p00(n=1):
    even=None
    # ↓程式區域↓
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

    # ↑程式區域↑
    return even