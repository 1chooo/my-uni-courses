# -*- coding: utf-8 -*-
"""
Date: 2023/11/06
Question: 08
Author: 林群賀
Student Number: 109601003
"""

initial_monthly_salary = 48200
annual_salary_increase = 0.035

monthly_salaries = []

year = 2023

standard = 1000000
tmp_year = []
flag = False

while True:

    total_salary = initial_monthly_salary * 13.5

    total_salary = round(total_salary)
    total_salary = int(total_salary)

    initial_monthly_salary = round(initial_monthly_salary)
    initial_monthly_salary = int(initial_monthly_salary)

    if year < 2033:
        print(f"{year} 年: 月薪為 {initial_monthly_salary} 元，該年總收入為 {total_salary} 元")

    year += 1
    initial_monthly_salary *= (1 + annual_salary_increase)

    if year == 2033:
        print(f"直到 {year - 1} 年底，林先生在該企業的總收入為 {total_salary} 元")

    if total_salary > standard:
        print(f"林先生工作到 {year} 年時，年收入會超過一百萬，該年收入為 {total_salary} 元")
        break

