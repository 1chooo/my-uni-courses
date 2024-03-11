# -*- coding: utf-8 -*-

import random

flag_int = random.randint(1, 100)
count_int = 0

while True :

    my_str = input('輸入一數字 : ')
    my_int = int(my_str)
    count_int += 1

    if my_int > flag_int :
        print('比', my_str, '還要小')
    elif my_int < flag_int :
        print('比', my_str, '還要大')
    else :
        print('猜對了！總共猜了', count_int, '次')
        break