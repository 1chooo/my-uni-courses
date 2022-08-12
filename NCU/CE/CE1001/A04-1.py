# -*- coding: utf-8 -*-

from __future__ import print_function

input_file = open('./CE1001/src/score.txt', 'r')
output_file = open('./CE1001/src/score_stu_id.txt', 'w')

list1 = input_file.readlines()
print(list1[0], end = ' ', file = output_file)

for i in range(1, len(list1)):
    avg_int = 0
    list2 = list1[i].split()
    a_int = int(list2[1])
    b_int = int(list2[2])
    c_int = int(list2[3])
    d_int = int(list2[4])
    avg_int = (a_int + b_int + c_int + d_int) / 4

    if i == len(list1) - 1:
        print(list2[0], list2[1], list2[2], list2[3], list2[4], avg_int, end = ' ', file = output_file)
        break

    print(list2[0], list2[1], list2[2], list2[3], list2[4], avg_int, file = output_file)

input_file.close()
output_file.close()