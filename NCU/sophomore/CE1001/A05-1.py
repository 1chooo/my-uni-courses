# -*- coding: utf-8 -*-

# 此函數為判斷是否輸入為 0 和 1
def is_in(bin_num):

    for i in bin_num:
        if i > '1' or i < '0':  # if i != '1' and i != '0'
            return False
    return True

# 此函數將 2 進位 轉換為 16 進位
def bin_To_hexa(bin_num):

    # 設定餐變數
    hex_str = ''
    bin_group = ''

    # 取四個一組，不夠四個的補 0
    if len(bin_num) % 4 != 0:
        bin_num = '0' * (4 - (len(bin_num) % 4)) + bin_num

    for i in range(len(bin_num)):
        if (i % 4 == 0) and (i != 0):
            bin_group += ' ' + bin_num[i]
        else:
            bin_group += bin_num[i]

    bin_group = bin_group.split(' ')

    for i in bin_group:
        a = (int(i[0]) * 2 ** 3) + (int(i[1]) * 2 ** 2) + (int(i[2]) * 2 ** 1) + (int(i[3]) * 2 ** 0)

        if a >= 0 and a <= 9:
            hex_str = hex_str + str(a)
        elif a == 10:
            hex_str = hex_str + 'A'
        elif a == 11:
            hex_str = hex_str + 'B'
        elif a == 12:
            hex_str = hex_str + 'C'
        elif a == 13:
            hex_str = hex_str + 'D'
        elif a == 14:
            hex_str = hex_str + 'E'
        elif a == 15:
            hex_str = hex_str + 'F'

    return hex_str


while True:
    bin_num = input('Binary: ')

    if is_in(bin_num):
        hex_str = bin_To_hexa(bin_num)
        print('Hexadecimal:', hex_str)
        continue
    elif bin_num == str(-1):
        break
    elif is_in(bin_num) == False:
        print('Not Binary Number !')
        continue