# -*- coding: utf-8 -*-
"""
Date: 2023/10/30
HW: 17
Author: 林群賀
Student Number: 109601003
"""

# Define principal and interest rate
principal = 42625
interest_rate = 0.0275  # 2.75% as a decimal

# Initialize variables to track total interest and principal over time
total_interest = 0
total_money = 0

# Calculate and print interest and total amount for each year
for year in range(1, 36):
    annual_interest = principal * interest_rate
    total_interest += annual_interest
    principal += annual_interest
    total_amount = principal
    total_money += total_amount
    print(f"Year {year}: Interest: ${annual_interest:.2f} Total Amount: ${total_amount:.2f} Total Money: ${total_money:.2f}")

# print(f"Total Interest over 35 years: ${total_interest:.2f}")

