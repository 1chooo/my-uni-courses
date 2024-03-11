# -*- coding: utf-8 -*-

def is_in(my1_str):
    for i in my1_str:
        if i > '1' or i < '0':  # if i!='1' and i!='0'
            return False
    return True

while True:

    my1_str = input('NUM(BIN) : ')

    if is_in(my1_str):
        my2_int = int(my1_str, 2)
        my3_int = 16 * my2_int
        print('NUM(DEC) after X16 :', my3_int)
        my2_str = oct(my3_int)
        print('NUM(OCT) :', my2_str[2:], '\n')
        continue
    elif my1_str == str(-1):
        break
    elif is_in(my1_str) == False:
        print('Not Binary Number !', '\n')
        continue