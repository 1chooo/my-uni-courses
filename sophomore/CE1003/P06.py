# -*- coding: utf-8 -*-

def recursive_function(num):

    # print(num)    確認數字進來為何
    if num <= 0:
        return 0
    elif num % 2 == 0:
        return 2 + recursive_function(num // 2)
    else:
        num_str = str(num)
        # print(num_str)    確認型態 debug 用
        num_sum = 0

        for i in range(0, len(num_str)):
            num_sum = num_sum + int(num_str[i])
        return 3 + recursive_function(num_sum - 5)

""" Main """

input_file = open('test_2.txt', 'r')

for line_str in input_file:
    num_int = int(line_str)
    # print(num_int)    確認型態 debug 用
    print(recursive_function(num_int))