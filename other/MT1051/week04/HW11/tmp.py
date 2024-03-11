# -*- coding: utf-8 -*-
"""
Date: 2023/10/02
HW: 11
Author: 林群賀
Student Number: 109601003
"""

# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f'{i} x {j} =', i * j)

class MultiplicationTable:
    def __init__(self, start_row=2, end_row=9, start_column=1, end_column=9):
        self.start_row = start_row
        self.end_row = end_row
        self.start_column = start_column
        self.end_column = end_column

    def generate_table(self):
        for i in range(self.start_row, self.end_row + 1):
            for j in range(self.start_column, self.end_column + 1):
                result = i * j
                print(f'{i} x {j} = {result}')

if __name__ == '__main__':
    table = MultiplicationTable()
    table.generate_table()
