# 匯入 keyword 模組
import keyword

# 列印關鍵字列表
print(keyword.kwlist)

# 檢查 'if' 是否是關鍵字，預期結果是 True
is_if_keyword = keyword.iskeyword('if')
print("Is 'if' a keyword?", is_if_keyword)

# 檢查 'IF' 是否是關鍵字，預期結果是 False
is_IF_keyword = keyword.iskeyword('IF')
print("Is 'IF' a keyword?", is_IF_keyword)

"""
"""

# 整數相加
result1 = 23 + 45
print(result1)

# 整數相減
result2 = 59 - 22
print(result2)

# 整數相乘
result3 = 43 * 3
print(result3)

# 整數平方
result4 = 8 ** 2
print(result4)

# 整數除法（浮點數結果）
result5 = 16 / 4
print(result5)

# 整數除法（整數結果）
result6 = 16 // 4
print(result6)

# 整數除法（浮點數結果）
result7 = 16 // 4.0
print(result7)

# 取餘數
result8 = 15 % 4
print(result8)

# 取餘數（浮點數結果）
result9 = 15 % 4.0
print(result9)

# 定義變數 x 並賦值
x = 5
print(x)

# 增加 x 的值
x = x + 1
print(x)

# 增加 x 的值（簡化語法）
x += 1
print(x)

# 遞減 x 的值
x -= 1
print(x)

# 負負得正
x = -x
print(x)

# 不支援後置遞減運算符 x--
# 定義變數 y 並賦值
y = 3
print(x, y)

# 將 y 的值提高到 x 的次方
y **= x
print(x, y)

# 大數計算
big_number1 = 33 ** 999
print(big_number1)

# 大數計算（浮點數結果）
big_number2 = 33.0 ** 999
print(big_number2)

"""
"""

# 整數 36
print(36)

# 二進位數字 0b1011，表示十進位的 11
print(0b1011)

# 八進位數字 0o36，表示十進位的 30
print(0o36)

# 十六進位數字 0x36，表示十進位的 54
print(0x36)

# 加法操作，包括十進位、二進位、八進位和十六進位
result = 11 + 0b11 + 0o11 + 0x11
print(result)

# 浮點數 31.2
print(312e-2)

# 將浮點數轉換為整數，結果是 31
int_result = int(312e-2)
print(int_result)

# 整數 20
print(20)

# 將整數轉換為浮點數，結果是 20.0
float_result = float(20)
print(float_result)

# 將浮點數 25.346 保留兩位小數，結果是 25.35
rounded_result = round(25.346, 2)
print(rounded_result)

# 定義整數變數 x，值為 33
x = 33
print("type(x) =", type(x))
print("id(x) =", id(x))
print("x =", x)

# 將變數 x 的值更改為浮點數 63.6
x = 63.6
print("type(x) =", type(x))
print("id(x) =", id(x))
print("x =", x)

print("abc".isidentifier()) # True
print("99a".isidentifier()) # False
print("_".isidentifier()) # True
print("for".isidentifier()) # True