# -*- coding: utf-8 -*-

def recursive_function(input_num):
    """ build recursive function """
    if input_num <= 4:
        return 3
    elif input_num in range(5, 10):
        return 2 + recursive_function(input_num - 2)
    elif input_num >= 10:
        return 1 + recursive_function(input_num - 22) + \
               recursive_function(recursive_function(input_num - 30) - 30)

while True:
    my_str = input('Please input the variable of F(N): ')

    if my_str == '0':
        break
    elif my_str.isdecimal():
        my_int = int(my_str)

        if my_int in range(1, 501):
            print(recursive_function(my_int))
        elif my_int > 0:
            print('Integer should less than or equal to 500!')
        else:   # if input is 00
            print('Input should be a positive integer!')
    else:
        print('Input should be a positive integer!')