# -*- coding: utf-8 -*-
"""
Date: 2023/10/23
Ultimate Code Game
Author: 林群賀
Student Number: 109601003
"""

import random

# 生成一個 4 位數的秘密數字
def generate_secret_number():
    return str(random.randint(1000, 9999))

# 比較玩家的猜測和秘密數字
def compare_numbers(secret, guess):
    if secret == guess:
        return "4A0B"  # 4A表示完全猜對，0B表示位置錯誤的數字數
    else:
        result = []
        for i in range(4):
            if secret[i] == guess[i]:
                result.append('A')
            elif secret[i] in guess:
                result.append('B')
        return ''.join(result)

# 遊戲主程式
def main():
    print("歡迎來到終極密碼遊戲！")
    secret_number = generate_secret_number()
    attempts = 0

    while True:
        guess = input("請輸入你的猜測 (4 位數字): ")
        attempts += 1

        if len(guess) != 4 or not guess.isdigit():
            print("請輸入有效的 4 位數字。")
            continue

        result = compare_numbers(secret_number, guess)

        print(f"結果：{result}")
        if result == "4A0B":
            print(f"恭喜你猜中了！秘密數字是 {secret_number}，你總共嘗試了 {attempts} 次。")
            break

if __name__ == "__main__":
    main()
