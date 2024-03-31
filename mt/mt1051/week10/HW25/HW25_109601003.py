# -*- coding: utf-8 -*-
"""
Date: 2023/11/27
HW: 25
Author: 林群賀
Student Number: 109601003
"""

def compound_interest(principal, rate, years):
    principals = [principal]  # 用來計算本金的 list
    compound = [principal]  # 第 0 年的本金

    for year in range(1, years + 1):
        principal += principal * rate  # 更新本金為前一年的本金加上利息
        compound.append(principal)
        principals.append(compound[year - 1])

    return principals, compound

initial_principal = 33500  # 初始本金
annual_interest_rate = 0.0225  # 年利率
investment_years = 25  # 投資年限

principals, result = compound_interest(initial_principal, annual_interest_rate, investment_years)

for i in range(len(result)):
    print(f"第 {i} 年本金: ${principals[i]:.2f} 期末本利和: ${result[i]:.2f}")
