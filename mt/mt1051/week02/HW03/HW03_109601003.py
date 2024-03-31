# -*- coding: utf-8 -*-
"""
Date: 2023/09/18
HW: 03
Author: 林群賀
Student Number: 109601003
"""

from typing import Any
import math

# print(((1.4 - 3.5) ** 2 + (8.3 - 12.7) ** 2) ** 0.5)
# print(math.sqrt((1.4 - 3.5) ** 2 + (8.3 - 12.7) ** 2))

# num = 1 / 2
# print("test:", ((1.4 - 3.5) ** 2 + (8.3 - 12.7) ** 2) ** num)

class HomeworkThree:

    point_A = (1.4, 8.3)
    point_B = (3.5, 12.7)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def __init__(self) -> None:
        pass

    def get_point_info(self, ):
        self.point_A_x = float(input("x1 = "))
        self.point_A_y = float(input("y1 = "))
        self.point_B_x = float(input("x2 = "))
        self.point_B_y = float(input("y2 = "))

    def get_distance(self,):
        x = self.point_A[0] - self.point_B[0]
        y = self.point_A[1] - self.point_B[1]

        distance = (x ** 2 + y ** 2) ** 0.5
        # distance = math.sqrt(x ** 2 + y ** 2)

        return round(distance, 2)
    
    def get_test_distance(self,):
        self.get_point_info()
        x = self.point_A_x - self.point_B_x
        y = self.point_A_y - self.point_B_y

        distance = (x ** 2 + y ** 2) ** 0.5
        # distance = math.sqrt(x ** 2 + y ** 2)

        return round(distance, 2)
    
homework_three = HomeworkThree()
# distance = homework_three.get_distance()

# print("Distance:", distance)

distance = homework_three.get_test_distance()
print("Distance with input value:", distance)
