# -*- coding: utf-8 -*-

input_file = open('./CE1001/src/score_stu_id.txt', 'r')

my1_str = input('查詢項目: ').capitalize()
my2_str = input('姓名: ').capitalize()
list1 = input_file.readlines()

for i in range(0, len(list1)):
    list2 = list1[i].split()
    name_str = list2[0]

    if i == 0:
        if my1_str in list2:
            order = list2.index(my1_str)
        else:
            break
    else:
        if my2_str == name_str:
            print(name_str, my1_str, list2[order])

input_file.close()