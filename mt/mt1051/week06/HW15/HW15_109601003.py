# -*- coding: utf-8 -*-
"""
Date: 2023/10/23
HW: 15
Author: 林群賀
Student Number: 109601003
"""

class CoinProblem:
    def __init__(self):
        self.num_10 = 0
        self.num_5 = 0
        self.num_1 = 0
        self.total_value = 0

    def calculate_coins(self):
        for self.num_10 in range(0, 21):
            for self.num_5 in range(0, 41):
                self.num_1 = 20 - self.num_10 - self.num_5

                if (
                    self.num_1 >= 0
                    and self.num_5 >= 0
                    and self.num_10 >= 0
                    and (self.num_10 * 10 + self.num_5 * 5 + self.num_1 == 108)
                ):
                    return

    def print_result(self):
        print("10 元硬幣數量：", self.num_10)
        print("5  元硬幣數量：", self.num_5)
        print("1  元硬幣數量：", self.num_1)

if __name__ == "__main__":
    coin_problem = CoinProblem()
    coin_problem.calculate_coins()
    coin_problem.print_result()
