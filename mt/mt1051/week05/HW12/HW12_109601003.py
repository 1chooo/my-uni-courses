# -*- coding: utf-8 -*-
"""
Date: 2023/10/16
HW: 12
Author: 林群賀
Student Number: 109601003
"""

# # Define the target function
# def target_function(x):
#     return 3 * x * x - 6 * x + 3

# # Define the range over which you want to search for the minimum
# # Adjust the range and step size as needed
# start_x = -10
# end_x = 10
# step = 0.01

# min_x = start_x
# min_y = target_function(start_x)

# for x in range(int(start_x * 100), int(end_x * 100)):
#     current_x = x / 100
#     current_y = target_function(current_x)
#     if current_y < min_y:
#         min_x = current_x
#         min_y = current_y

# print(f"for loop - min: x = {min_x}, y = {min_y}")

# Define the target function
def target_function(x):
    return 3 * x * x - 6 * x + 3

start_x = -10
end_x = 10
step = 0.01

min_x = start_x
min_y = target_function(start_x)

current_x = start_x

while current_x <= end_x:
    current_y = target_function(current_x)
    if current_y < min_y:
        min_x = current_x
        min_y = current_y
    current_x += step

print(f"(1). min: x = {min_x}, y = {min_y}")

# Define the target function
def target_function(x):
    return 1/2 * x * x - 3 * x + 7/2

# Define the range over which you want to search for the minimum
# Adjust the range and step size as needed
start_x = -10
end_x = 10
step = 0.01

min_x = start_x
min_y = target_function(start_x)

current_x = start_x

while current_x <= end_x:
    current_y = target_function(current_x)
    if current_y < min_y:
        min_x = current_x
        min_y = current_y
    current_x += step

print(f"(2). min: x = {min_x}, y = {min_y}")
