# -*- coding: utf-8 -*-

input_file_1 = open("./CE1001/src/invoice.txt", "r")
input_file_2 = open("./CE1001/src/num_2.txt", "r")

list1 = input_file_1.read().splitlines()
list2 = input_file_2.read().splitlines()    # 對獎號

sumPrice, a, b, c, d, e, f, g, h, N = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

for i in range(0, len(list1)):
    if list1[i] == list2[0]:
        sumPrice += 10000000
        a += 1
        continue
    elif list1[i] == list2[1]:
        sumPrice += 2000000
        b += 1
        continue
    elif list1[i] == list2[2] or list1[i] == list2[3] or list1[i] == list2[4]:
        sumPrice += 200000
        c += 1
        continue
    elif list1[i][1:] == list2[2][1:] or list1[i][1:] == list2[3][1:] or list1[i][1:] == list2[4][1:]:
        sumPrice += 40000
        d += 1
        continue
    elif list1[i][2:] == list2[2][2:] or list1[i][2:] == list2[3][2:] or list1[i][2:] == list2[4][2:]:
        sumPrice += 10000
        e += 1
        continue
    elif list1[i][3:] == list2[2][3:] or list1[i][3:] == list2[3][3:] or list1[i][3:] == list2[4][3:]:
        sumPrice += 4000
        f += 1
        continue
    elif list1[i][4:] == list2[2][4:] or list1[i][4:] == list2[3][4:] or list1[i][4:] == list2[4][4:]:
        sumPrice += 1000
        g += 1
        continue
    elif list1[i][5:] == list2[2][5:] or list1[i][5:] == list2[3][5:] or list1[i][5:] == list2[4][5:]\
            or list1[i][5:] == list2[5] or list1[i][5:] == list2[6] or list1[i][5:] == list2[7]:
        sumPrice += 200
        h += 1
        continue
    else:
        N += 1

print("特別獎：", a)
print("特獎：", b)
print("頭獎：", c)
print("二獎：", d)
print("三獎：", e)
print("四獎：", f)
print("五獎：", g)
print("六獎：", h)
print("沒中獎：", N)
print(sumPrice)

input_file_1.close()
input_file_2.close()