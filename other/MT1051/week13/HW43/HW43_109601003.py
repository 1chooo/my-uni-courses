# -*- coding: utf-8 -*-
"""
Date: 2023/12/18
HW: 43
Author: 林群賀
Student Number: 109601003
"""

# def compound_interest(principal, rate, years):
#     principals = [principal]  # 用來計算本金的 list
#     compound = [principal]  # 第 0 年的本金

#     for year in range(1, years + 1):
#         principal += principal * rate  # 更新本金為前一年的本金加上利息
#         compound.append(principal)
#         principals.append(compound[year - 1])

#     return principals, compound

# initial_principal = 33500  # 初始本金
# annual_interest_rate = 0.0225  # 年利率
# investment_years = 25  # 投資年限

# principals, result = compound_interest(initial_principal, annual_interest_rate, investment_years)

# for i in range(len(result)):
#     print(f"第 {i} 年本金: ${principals[i]:.2f} 期末本利和: ${result[i]:.2f}")

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(0, 26, 1)
# plt.plot(x, principals, lw=3)
# plt.plot(x, result, lw=3)
# plt.legend(['principal', 'Benefit and Benefit'], loc='upper left', fontsize=14)
# plt.xlabel("year", fontsize=10)
# plt.ylabel("dollar", fontsize=10)
# plt.title("HW39 Compound Interest", fontsize=14)
# plt.grid(True)

# plt.show()


# def compound_interest(principal, rate, years):
#     principals = [principal]  # 用來計算本金的 list
#     compound = [principal]  # 第 0 年的本金

#     for year in range(1, years + 1):
#         principal += principal * rate  # 更新本金為前一年的本金加上利息
#         compound.append(principal)
#         principals.append(compound[year - 1])

#     return principals, compound

# initial_principal = 33500  # 初始本金
# annual_interest_rate = 0.0225  # 年利率
# investment_years = 25  # 投資年限

# principals, result = compound_interest(initial_principal, annual_interest_rate, investment_years)

# # Write the results to a text file
# with open('compound_interest_results.txt', 'w') as file:
#     for i in range(len(result)):
#         file.write(f"第 {i} 年本金: ${principals[i]:.2f} 期末本利和: ${result[i]:.2f}\n")

# print("Results have been written to 'compound_interest_results.txt'.")


def compound_interest(principal, rate, years):
    periods = []  # 期數
    principals = []  # 本金
    compound = []  # 期末終值

    for year in range(years):
        periods.append(year + 1)
        principals.append(principal)
        principal += principal * rate
        compound.append(principal)

    return periods, principals, compound

initial_principal = 33500  # 初始本金
annual_interest_rate = 0.0225  # 年利率
investment_years = 25  # 投資年限

periods, principals, result = compound_interest(initial_principal, annual_interest_rate, investment_years)

# Write the results to a text file
with open('compound_interest_results.txt', 'w') as file:
    file.write("periods, principals, result\n")
    for i in range(len(result)):
        file.write(f"{periods[i]}, {principals[i]:.2f}, {result[i]:.2f}\n")

print("Results have been written to 'compound_interest_results.txt'.")
