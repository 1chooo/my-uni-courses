# 定義字串 s1
s1 = 'hello'

# 輸出 s1
print("s1:", s1)

# 輸出 s1 的類型
print("Type of s1:", type(s1))

# 輸出 s1 的ID
print("ID of s1:", id(s1))

# 輸出 s1 的第一個和第四個字符
print("s1[0]:", s1[0])
print("s1[3]:", s1[3])

# 修改 s1 的值
s1 = 'python'

# 輸出修改後的 s1
print("s1:", s1)

# 輸出修改後 s1 的ID
print("ID of modified s1:", id(s1))

# 輸出 s1 的最後一個和倒數第三個字符
print("s1[-1]:", s1[-1])
print("s1[-3]:", s1[-3])

"""
"""

# 定義字串 s2
s2 = 'Python Basics'

# 使用切片操作取得不同部分的子字串
print("s2[:] =", s2[:])           # 取得整個字串
print("s2[4:] =", s2[4:])         # 從索引4開始到結尾
print("s2[:-2] =", s2[:-2])       # 從開頭到倒數第三個字符（不包括倒數第二個字符）
print("s2[:11] =", s2[:11])       # 從開頭到索引11（不包括索引11）
print("s2[2:-1] =", s2[2:-1])     # 從索引2到倒數第二個字符（不包括倒數第一個字符）
print("s2[3:8:2] =", s2[3:8:2])   # 從索引3到索引8，步幅為2

# 檢查 'y' 是否在 s2 中
print("'y' in s2 =", 'y' in s2)

# 取得 s2 的長度
print("len(s2) =", len(s2))

"""
"""
# 定義字串 s3
s3 = '###PYTHON###'

# 使用字串方法執行各種操作
lower_case = s3.lower()        # 轉換為小寫
lstrip_result = s3.lstrip('#')  # 刪除左側的 '#' 字元
rstrip_result = s3.rstrip('#')  # 刪除右側的 '#' 字元
strip_result = s3.strip('#')    # 刪除兩側的 '#' 字元

# 輸出結果
print("s3.lower() =", lower_case)
print("s3.lstrip('#') =", lstrip_result)
print("s3.rstrip('#') =", rstrip_result)
print("s3.strip('#') =", strip_result)

"""
"""
name = 'Benjamin'
age = 18

print(name + ' is ' + str(age) + ' years old.')
print(name, 'is', age, 'years old.')

data = input('Enter a number : ')
print('You entered:', data)

data = int(input('Enter a number : '))
print('You entered (as integer):', data)

data = eval(input('Enter a number : '))
print('You entered (as evaluated expression):', data)

data = eval(input('Enter expression : '))
print('Result of the expression:', data)

"""
"""

name = 'LabVIEW360'
est = 2000

result = f'{name} was established in {est}.'
print(result)

"""
"""

from datetime import datetime

datetime.now()
