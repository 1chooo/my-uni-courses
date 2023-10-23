# -*- coding: utf-8 -*-
"""
Date: 2023/10/23
HW: 14
Author: 林群賀
Student Number: 109601003
"""

# Initial monthly salary and annual salary increase rate
initial_monthly_salary = 48200  # Initial monthly salary
annual_salary_increase = 0.035  # Annual salary increase rate (3.5%)

# Number of years and months
years = 25
months_per_year = 12

# Initial working date and month
start_date = "2023-01-01"  # Start working from January 1, 2023

# Initialize variables
current_salary = initial_monthly_salary
total_income = 0

# Calculate monthly salary and total income for the next 25 years
year = 2023
month = 1

while total_income <= 1025000:
    # Calculate total income for the current month
    total_income += current_salary

    # Print the monthly salary and total income for the current month
    # print(f"Year: {year}, Month: {month}, Monthly Salary: {current_salary}, Total Income: {total_income}")

    # Update the monthly salary (annual salary increase)
    current_salary *= (1 + annual_salary_increase)

    # Update the year and month
    month += 1
    if month > months_per_year:
        month = 1
        year += 1

print(f"Year: {year}, Month: {month}, Total income exceeded 1025000. Stopping the loop.")

# Initial monthly salary and annual salary increase rate
initial_monthly_salary = 48200  # Initial monthly salary
annual_salary_increase = 0.035  # Annual salary increase rate (3.5%)

# Initialize variables
current_salary = initial_monthly_salary
total_income = 0
year = 2023
month = 1

# Find the year and month when monthly salary exceeds 115,000
while current_salary <= 115000 and year < 2048:  # Assuming no salary will exceed 115,000 after 2048
    # Update the current salary (annual salary increase)
    current_salary *= (1 + annual_salary_increase)
    year += 1

# Print the year and month when monthly salary exceeds 115,000
if year < 2048:
    print(f"The monthly salary will exceed $115,000 in {year}-{month:02d}")
else:
    print("The monthly salary will not exceed $115,000 in the next 25 years.")
