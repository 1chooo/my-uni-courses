# -*- coding: utf-8 -*-
"""
Date: 2023/10/23
Ultimate Code Game
Author: 林群賀
Student Number: 109601003
"""

import random

low = 1
high = 100
ans = random.randint(low + 1, high - 1)

guessed = False

while not guessed:
    num = int(input(f'請輸入猜測的數字: ({low} ~ {high})'))

    if num <= low or num >= high:
        print('你亂猜的吧?')
        continue
    elif num == ans:
        print('恭喜你猜對了!')
        guessed = True
    elif num < ans:
        low = num
        print('太小了!')
    else:
        high = num
        print('太大了!')
