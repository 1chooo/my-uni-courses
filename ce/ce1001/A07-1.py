# -*- coding: utf-8 -*-

input_file = open('./CE1001/src/seat.txt', 'r')
list1 = input_file.read()
list1_split = list1.split('1')
list1_s = list(list1)

list1_len = []
for i in list1_split:
    list1_len.append(len(i))

max_value = max(list1_len)
L = 0
if max_value % 2 == 0:
    L = max_value // 2
else:
    L = (max_value // 2) + 1

d = 0                           # 判斷與 1 的距離
L_list = []
list1_len = len(list1)
for i in range(list1_len):
    if list1_s[i] == '1':       # 遇到 1 歸零
        d = 0
    elif list1_s[i] == '0':     # 遇到 0 加一
        d += 1

    # 只找 2L 跟 2L-1
    if d == 2 * L:
        L_list.append(i - L + 1)    # 遇到 d = 2L，往左減去 L 補 1
    elif d == ((2 * L) - 1):
        L_list.append(i - L + 1)    # 遇到 d = 2L，往左減去 L 補 1

print("L =", L, ",", "i =", L_list)
input_file.close()