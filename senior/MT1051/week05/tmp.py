# -*- coding: utf-8 -*-
"""
Date: 2023/10/16
HW: 12
Author: 林群賀
Student Number: 109601003
"""

N = 1
total = 0

while total <= 20:
    total += N
    if total > 20:
        break
    N += 1

print("N =", N)

GREATER = False

min_value = 9999
x = -20.0
y = -1
while y < min_value:
    min_value = y
    x += 0.01
    y = 3 * x * x - 6 * x + 3

print("min:", min_value)
print("x:", x)

from scipy.optimize import minimize_scalar

# 定义目标函数
def target_function(x):
    return 3 * x * x - 6 * x + 3

result = minimize_scalar(target_function)

min_x = result.x
min_y = result.fun

print(f"min: x = {min_x}, y = {min_y}")

# Define the target function
def target_function(x):
    return 3 * x * x - 6 * x + 3

# Define the range over which you want to search for the minimum
# You can adjust the range as needed
x_range = [i/100 for i in range(-1000, 1001)]  # This creates a range from -10 to 10 in steps of 0.01

# Find the minimum value of the function
min_x = min(x_range, key=target_function)
min_y = target_function(min_x)

print(f"min: x = {min_x}, y = {min_y}")

# Define the target function
def target_function(x):
    return 3 * x * x - 6 * x + 3

# Define the range over which you want to search for the minimum
# Adjust the range and step size as needed
start_x = -10
end_x = 10
step = 0.01

min_x = start_x
min_y = target_function(start_x)

for x in range(int(start_x * 100), int(end_x * 100)):
    current_x = x / 100
    current_y = target_function(current_x)
    if current_y < min_y:
        min_x = current_x
        min_y = current_y

print(f"min: x = {min_x}, y = {min_y}")

