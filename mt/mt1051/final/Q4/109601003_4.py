# -*- coding: utf-8 -*-
"""
Date: 2023/12/25
Question: 04
Author: 林群賀
Student Number: 109601003
有用 ChatGPT
"""

from datetime import datetime

first_day = datetime(2023, 9, 11, 0, 0, 0)
final_exam = datetime(2023, 12, 25, 0, 0, 0)

year = int(input("請輸入年份: "))
month = int(input("請輸入月份: "))
day = int(input("請輸入日期: "))

my_date = datetime(year, month, day)

# 1. 請輸出 "本學期已經過 %d 天"
days_passed = (my_date - first_day).days

print("Q1:")
print(f"本學期已經過 {days_passed} 天")


print("Q2:")
# 2. 判斷 my_date 與 final_exam 的關係並輸出對應訊息
if my_date < final_exam:
    days_to_final_exam = (final_exam - my_date).days
    print(f"距離期末考還有 {days_to_final_exam} 天")
elif my_date > final_exam:
    days_since_final_exam = (my_date - final_exam).days
    print(f"期末考已經結束 {days_since_final_exam} 天前")
else:
    print("今天就是期末考！")
