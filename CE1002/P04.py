# -*- coding: utf-8 -*-

from __future__ import print_function

input_file = open("./CE1002/src/test_1.txt", 'r')
output_file = open('./CE1002/src/ans-stu_id.txt', 'w')

for line_str in input_file:         # read one line at once
    line_str = line_str.split()     # separate with each string

    a_str = line_str[0]
    b_str = line_str[2]
    c_str = line_str[4]
    a_int = int(a_str)
    b_int = int(b_str)
    c_int = int(c_str)

    """ To check whether the answer is true"""
    if line_str[1] == '+':
        real_ans_int = a_int + b_int
        if real_ans_int == c_int:
            print('T', file = output_file)
        else:
            print('F', file = output_file)
    elif line_str[1] == '-':
        real_ans_int = a_int - b_int
        if real_ans_int == c_int:
            print('T', file = output_file)
        else:
            print('F', file = output_file)
    elif line_str[1] == '*':
        real_ans_int = a_int * b_int
        if real_ans_int == c_int:
            print('T', file = output_file)
        else:
            print('F', file = output_file)

input_file.close()
output_file.close()