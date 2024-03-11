# -*- coding: utf-8 -*-

from __future__ import print_function

input_file = open('./CE1001/src/num.txt', 'r')
output_file = open('./CE1001/src/stu_id_1.txt', 'w')
str_1 = input_file.read()
int_1 = int(str_1)
list = []
string = ""
left = right = int_1

def well_formed(string, list, left, right):
    if right == 0:
        output_file.write(string + " ")

    if left > 0:
        well_formed(string + "(", list, left-1, right)

    if right > left and right > 0:
        well_formed(string + ")", list, left, right-1)

if int_1 == 0:
    print("none", end = "", file = output_file)
well_formed(string, list, left, right)
output_file.write("\n" + "stu_id_name")
input_file.close()
output_file.close()

# result = []
#
# def backtrack(路徑, 選擇列表):
#     if 滿足結束條件:
#         result.add(路徑)
#         return
#
#     for 選擇 in 選擇列表:
#         做選擇
#         backtrack(路徑, 選擇列表)
#         撤銷選擇