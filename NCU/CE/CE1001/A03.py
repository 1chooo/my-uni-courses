# -*- coding: utf-8 -*-

# find the factor first then disguise whether they are prime

def find_factor(factor_str):
    factor_int = int(factor_str)
    list1 = []                          # list1 為存放因數的字串

    for i in range(1, factor_int + 1):  # 一算到自己本身
        if factor_int % i == 0:
            list1.append(i)             # 丟到 list1
    return list1

def find_prime(prime_str):
    prime_int = int(prime_str)

    if prime_int == 1:
        return 'N'
    elif prime_int == 2:
        return 'Y'
    else:
        for i in range(2, prime_int):
            if prime_int % i == 0:
                return 'N'
        return 'Y'

# read the content from test.txt
file = open("./CE1001/src/test.txt", 'r')
all = file.read().split()
print(all)

file.close()

# take the output into the answer.txt
answer = open("./CE1001/src/answer.txt", 'w')
for i in all:
    answer.write('Number_' + str(all.index(i) + 1) + ': ' + str(i) + '\n')
    for j in find_factor(i):
        answer.write(str(j) + '  ' + str(find_prime(j)) + '\n')

answer.close()