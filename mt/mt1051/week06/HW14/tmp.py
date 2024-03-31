# -*- coding: utf-8 -*-
"""
Date: 2023/10/16
HW: 14
Author: 林群賀
Student Number: 109601003
"""

# Initial monthly salary and annual salary increase rate
initial_monthly_salary = 48200  # Initial monthly salary
annual_salary_increase = 0.035  # Annual salary increase rate (3.5%)

# Desired salary thresholds
desired_monthly_salary = 115000  # Desired monthly salary
desired_annual_salary = 1025000  # Desired annual salary

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
years_to_reach_monthly_goal = None
years_to_reach_annual_goal = None

# Calculate monthly salary and total income for the next 25 years using a while loop
year = start_year
while year < start_year + years:
    month = 1
    while month <= months_per_year:
        # Calculate total income for the current month
        total_income += current_salary
        # Check if monthly salary exceeds the desired monthly salary
        if current_salary >= desired_monthly_salary and years_to_reach_monthly_goal is None:
            years_to_reach_monthly_goal = year
            print(f"Monthly Salary Exceeds $115,000 in {year}-{month:02d}")
        # Update the monthly salary (annual salary increase)
        current_salary *= (1 + annual_salary_increase)
        month += 1
    
    if total_income >= desired_annual_salary and years_to_reach_annual_goal is None:
        years_to_reach_annual_goal = year
        print(f"Annual Salary Exceeds $1,025,000 in Year {year}")
    
    if years_to_reach_monthly_goal is not None and years_to_reach_annual_goal is not None:
        break

    year += 1

# Print the total income after 25 years
print(f"Total income after 25 years: ${total_income:.2f}")
