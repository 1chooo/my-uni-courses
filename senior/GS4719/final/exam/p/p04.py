def p04(input=2):
    # 定義數字對應的字母表
    num_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    # 輸出結果的列表
    output_list = []

    if input is None:
        return output_list

    # 定義遞迴函數來生成組合
    def generate_combinations(current_combination, remaining_digits):
        # 如果沒有剩餘的數字，將目前的組合加入結果列表
        if len(remaining_digits) == 0:
            output_list.append(current_combination)
            return
        
        # 取得目前最左邊的數字
        current_digit = remaining_digits[0]
        
        # 將該數字所對應的字母逐一加入目前的組合，並遞迴處理剩餘數字
        for letter in num_to_letters[current_digit]:
            generate_combinations(current_combination + letter, remaining_digits[1:])

    # 呼叫遞迴函數開始生成組合
    generate_combinations('', str(input))

    return output_list

# 測試範例
print(p04(23))  # Example 1
print(p04(None))  # Example 2
print(p04(2))  # Example 3
