# -*- coding: utf-8 -*-
"""
Date: 2023/09/18
HW: 02
Author: 林群賀
Student Number: 109601003
"""

from typing import Any

class QuestionOne:
    bottom = 2.5
    height = 3.6

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def __init__(self) -> None:
        pass

    def get_bottom(self, ):
        return self.bottom
    
    def get_height(self, ):
        return self.height

    def get_area(self, ):
        area = self.get_bottom() * self.get_height() / 2

        return area

class QuestionTwo:
    radius = 2.8 / 2
    PI = 3.14159

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def __init__(self) -> None:
        pass

    def get_radius(self, ):
        return self.radius
    
    def get_PI(self, ):
        return self.PI
    
    def get_area(self, ):
        area = self.radius ** 2 * self.get_PI()

        return round(area, 2)

class QuestionThree:

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    traingle_1_bottom = 1.6
    traingle_1_height = 2.2

    traingle_2_bottom = 2.6
    traingle_2_height = 3.2

    traingle_3_bottom = 3.6
    traingle_3_height = 4.5


    def __init__(self) -> None:
        pass

    def get_traingle_1_bottom(self,):
        return self.traingle_1_bottom
    
    def get_traingle_1_height(self,):
        return self.traingle_1_height

    def get_triangle_1_area(self,):
        triangle_1_area = (self.get_traingle_1_bottom() * self.get_traingle_1_height()) / 2

        return triangle_1_area
    
    def get_traingle_2_bottom(self,):
        return self.traingle_2_bottom
    
    def get_traingle_2_height(self,):
        return self.traingle_2_height
    
    def get_triangle_2_area(self,):
        triangle_2_area = (self.get_traingle_2_bottom() * self.get_traingle_2_height()) / 2

        return triangle_2_area
    
    def get_traingle_3_bottom(self,):
        return self.traingle_3_bottom
    
    def get_traingle_3_height(self,):
        return self.traingle_3_height
    
    def get_triangle_3_area(self,):
        triangle_3_area = (self.get_traingle_3_bottom() * self.get_traingle_3_height()) / 2

        return triangle_3_area
    
    def get_total_area(self, ):
        total_area = self.get_triangle_1_area() + self.get_triangle_2_area() + self.get_triangle_3_area()
        
        return round(total_area, 2)

class QuestionFour:

    external_radius = 3.2 / 2
    internal_radius = 1.5 / 2
    height = 6.8
    PI = 3.14159

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def __init__(self) -> None:
        pass

    def get_external_radius(self,):
        return self.external_radius
    
    def get_internal_radius(self,):
        return self.internal_radius
    
    def get_external_area(self,):
        external_area = self.external_radius ** 2

        return external_area
    
    def get_internal_area(self,):
        internal_area = self.internal_radius ** 2

        return internal_area
    
    def get_top_area(self,):
        top_area = self.get_external_area() - self.get_internal_area()
        
        return top_area
    
    def get_height(self,):
        return self.height
    
    def get_volume(self,):
        volume = (self.get_top_area() * self.PI * self.get_height())

        return round(volume, 2)
    
question_one = QuestionOne()
question_two = QuestionTwo()
question_three = QuestionThree()
question_four = QuestionFour()

area_one = question_one.get_area()
area_two = question_two.get_area()
area_three = question_three.get_total_area()
area_four = question_four.get_volume()

print("1.", area_one)
print("2.", area_two)
print("3.", area_three)
print("4.", area_four)
