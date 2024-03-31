# -*- coding: utf-8 -*-
"""
Date: 2023/10/02
HW: 08
Author: 林群賀
Student Number: 109601003
"""

class GradeCalculator:
    def __init__(self):
        self.grade_mapping = {
            (90, 100): 'A',
            (80, 89): 'B',
            (70, 79): 'C',
            (60, 69): 'D',
            (0, 59): 'F'
        }

    def calculate_grade(self, student_score):
        for score_range, grade in self.grade_mapping.items():
            if score_range[0] <= student_score <= score_range[1]:
                return grade
        return 'Invalid score'
    
import unittest

class TestGradeCalculator(unittest.TestCase):
    def test_calculate_grade(self):
        calculator = GradeCalculator()
        self.assertEqual(calculator.calculate_grade(95), 'A')
        self.assertEqual(calculator.calculate_grade(85), 'B')
        self.assertEqual(calculator.calculate_grade(75), 'C')
        self.assertEqual(calculator.calculate_grade(65), 'D')
        self.assertEqual(calculator.calculate_grade(55), 'F')
        self.assertEqual(calculator.calculate_grade(105), 'Invalid score')
        self.assertEqual(calculator.calculate_grade(-5), 'Invalid score')

if __name__ == "__main__":
    calculator = GradeCalculator()
    student_score = int(input("Enter the student's score: "))
    result = calculator.calculate_grade(student_score)
    print(result)

    # unittest.main()
