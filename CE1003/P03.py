# -*- coding: utf-8 -*-

def create_file():

    my_str = input('Create a file: ')
    my1_str = input('Write something: ')
    my_str = "./CE1002/src/" + my_str

    file = open(my_str, 'w')
    file.write(my1_str)
    file = open(my_str, 'r')
    my2_str = file.read()

    print('File name:', my_str)
    print('Context:', my2_str)

    file.close()

create_file()