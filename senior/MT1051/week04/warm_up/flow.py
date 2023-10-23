# -*- coding: utf-8 -*-
"""
Date: 2023/10/02
HW: 08
Author: 林群賀
Student Number: 109601003
"""

from typing import Any

class GradeCalculator:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def __init__(self) -> None:
        pass

    def score_standard(self, student_score, ) -> None:
        if student_score >= 90:
            print('GRADE = A')
        elif student_score >= 80:
            print('GRADE = B')
        elif student_score >= 70:
            print('GRADE = C')
        elif student_score >= 60:
            print('GRADE = D')
        else:
            print('GRADE = F')

    def get_student_score(self, ) -> int:
        student_score = int(input("Enter the student's score: "))

        return student_score
    
    def get_score(self, ) -> None:
        student_score = self.get_student_score()
        self.score_standard(student_score)

def main() -> None:
    grader_calculator = GradeCalculator()
    grader_calculator.get_score()
    
if __name__ == '__main__':
    main()
