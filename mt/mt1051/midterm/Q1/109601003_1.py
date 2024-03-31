# -*- coding: utf-8 -*-
"""
Date: 2023/11/06
Question: 01
Author: 林群賀
Student Number: 109601003
"""

total_projects = 9
total_developers = 30

developers_per_short_term_project = 2
developers_per_long_term_project = 4

short_term_projects = 0
long_term_projects = 0

for short_term_count in range(total_projects + 1):
    long_term_count = total_projects - short_term_count
    if (
        short_term_count * developers_per_short_term_project +
        long_term_count * developers_per_long_term_project == total_developers
    ):
        short_term_projects = short_term_count
        long_term_projects = long_term_count
        break

print(f"短期專案数量: {short_term_projects}")
print(f"長期專案数量: {long_term_projects}")
