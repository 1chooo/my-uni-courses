# -*- coding: utf-8 -*-
"""
Date: 2023/10/16
HW: 13
Author: 林群賀
Student Number: 109601003
"""

# Initial monthly salary and annual salary increase rate
initial_monthly_salary = 48200  # Initial monthly salary
# initial_monthly_salary = 46000  # Initial monthly salary
annual_salary_increase = 0.035  # Annual salary increase rate (3.5%)

# Number of years and months
years = 25
months_per_year = 12

# Initial working date and month
start_date = "2023-01-01"  # Start working from January 1, 2023
start_year = 2023
start_month = 1

# Initialize variables
current_salary = initial_monthly_salary
total_income = 0

# Calculate monthly salary and total income for the next 25 years
for year in range(start_year, start_year + years):
    for month in range(1, months_per_year + 1):
        # Calculate total income for the current month
        total_income += current_salary
        # Print the monthly salary and total income for the current month
        print(f"{year}-{month:02d}: Monthly Salary: ${current_salary:.2f}")
        # Update the monthly salary (annual salary increase)
        current_salary *= (1 + annual_salary_increase)
    print(f"Year {year}: Total Income: ${total_income:.2f}")

# Print the total income after 25 years
print(f"Total income after 25 years: ${total_income:.2f}")
