# -*- coding: utf-8 -*-
"""
Date: 2023/11/20
HW: 23
Author: 林群賀
Student Number: 109601003
"""

def count_depreciation():
    init = 100000
    rate = 9000

    for i in range(1, 11):
        print(f"年度 {i}, 折舊費用為 {rate}, 累積折舊為 {rate * i}, 期末帳面價值為 {init - rate * i}")

def main():
    count_depreciation()

if __name__ == "__main__":
    main()
