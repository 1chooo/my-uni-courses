# -*- coding: utf-8 -*-

from __future__ import print_function

input_file = open('./CE1001/src/digit.txt', 'r')
output_file = open('./CE1001/src/stu_id_2.txt', 'w')
num = input_file.read()
num = list(num)
num_len = len(num)

my_dict = {'1': 'none', '2': 'abc', '3': 'def',
           '4': 'ghi',  '5': 'jkl', '6': 'mno',
           '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

if num_len == 1:
    if num[0] == '1':
        print("none", end = '', file=output_file)
    else:
        for i in my_dict[num[0]]:
            print(i, end=' ', file=output_file)
if num_len == 2:
    for i in my_dict[num[0]]:
        for j in my_dict[num[1]]:
            print(i + j, end = ' ', file=output_file)
if num_len == 3:
    for i in my_dict[num[0]]:
        for j in my_dict[num[1]]:
            for k in my_dict[num[2]]:
                print(i + j + k, end = ' ', file=output_file)
if num_len == 4:
    for i in my_dict[num[0]]:
        for j in my_dict[num[1]]:
            for k in my_dict[num[2]]:
                for l in my_dict[num[3]]:
                    print(i + j + k + l, end = ' ', file=output_file)
if num_len == 5:
    for i in my_dict[num[0]]:
        for j in my_dict[num[1]]:
            for k in my_dict[num[2]]:
                for l in my_dict[num[3]]:
                    for m in my_dict[num[4]]:
                        print(i + j + k + l + m, end = ' ', file=output_file)
if num_len == 6:
    for i in my_dict[num[0]]:
        for j in my_dict[num[1]]:
            for k in my_dict[num[2]]:
                for l in my_dict[num[3]]:
                    for m in my_dict[num[4]]:
                        for n in my_dict[num[5]]:
                            print(i + j + k + l + m + n, end = ' ', file=output_file)

print("\nstu_id_name", end = "", file=output_file)
input_file.close()
output_file.close()