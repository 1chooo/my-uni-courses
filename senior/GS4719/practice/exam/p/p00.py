# def p00(n=1):
#     even=None
#     # ↓程式區域↓

#     # ↑程式區域↑
#     return even

def p00(n=1):
    prime = True

    if n <= 1:
        prime = False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                prime = False
                break

    return prime


if __name__ == "__main__":
    num = int(input("請輸入一個數字："))
    result = p00(num)
    print(result)
