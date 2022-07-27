# -*- coding: utf-8 -*-

# 此函數為判斷是否輸入為 0 和 1
def is_in(bin_num):

    for i in bin_num:
        if i != '1' and i != '0' and i != '+' and i != '-':
            return False

    return True

def binary_add(a, b):

    count_a = -1
    count_b = -1
    a_inverse = a[::-1]
    b_inverse = b[::-1]
    a_dec = 0
    b_dec = 0

    for i in a_inverse:
        count_a += 1
        a_dec += int(i) * 2 ** count_a
    for i in b_inverse:
        count_b += 1
        b_dec += int(i) * 2 ** count_b

    sum = a_dec + b_dec

    if sum == 0:
        return "0"

    out = []
    while sum > 1:
        res = int(sum) % 2
        out.insert(0, str(res))
        sum = sum / 2

    return ''.join(out)

def binary_minus(a, b):

    count_a = -1
    count_b = -1
    a_inverse = a[::-1]
    b_inverse = b[::-1]
    a_dec = 0
    b_dec = 0

    for i in a_inverse:
        count_a += 1
        a_dec += int(i) * 2 ** count_a
    for i in b_inverse:
        count_b += 1
        b_dec += int(i) * 2 ** count_b

    sum = a_dec - b_dec

    if sum == 0:
        return "0"

    out = []
    while sum > 1:
        res = int(sum) % 2
        out.insert(0, str(res))
        sum = sum / 2

    return ''.join(out)

while True:
    bin_num = input()

    if bin_num == str(-1):
        break
    elif is_in(bin_num) and '+' in bin_num:
        bin_num = bin_num.split('+')
        answer_add = binary_add(bin_num[0], bin_num[1])
        print(answer_add)
        continue
    elif is_in(bin_num) and '-' in bin_num:
        bin_num = bin_num.split('-')
        answer_minus = binary_minus(bin_num[0], bin_num[1])
        print(answer_minus)
        continue