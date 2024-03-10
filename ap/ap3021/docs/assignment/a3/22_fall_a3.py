# %% [markdown]
# # [2022 Fall] Assignment3
# 
# > Course: AP3021

# %%
# -*-coding: utf-8 -*-

"""
Course: AP3021
Assignment: 3
Student id: 109601003
Name: 林群賀
"""

import math

# Build the factorial mechanism 

def factorial(n) :
    sum = 1

    for i in range(2, n + 1) :
        sum *= i

    return sum


#Build the error criterion : εs

def countErrorCriterion(n) :
    error_criterion = (0.5 * 10 ** (2 - n)) * 100

    return error_criterion


# Build the approximate estimate of the error : εa

def countApproximateEstimateError(current_approximation, previous_approximation) :
    approximate_error = current_approximation - previous_approximation

    if current_approximation == 0 :    # The first and second value of cosine tylor polynomial is 0.0 and 1.0; therefore we have to pass them.
        return 999
    else :
        approximate_estimate_error = abs((approximate_error / current_approximation) * 100)

    return approximate_estimate_error


# Build the percent relative error : εt

def countPercentRelativeError(true_value, approximation) :
    true_error = true_value - approximation
    percent_relative_error = (true_error / true_value) * 100

    return percent_relative_error


# Count the machine epsilon

def countMachineEpsilon() :
    epsilon = 1.0

    while (epsilon > 0) :
        xmin = epsilon
        epsilon = epsilon / 2

    return xmin


# Build cosine tylor polynomial

def cosineTylorPolynomial(n, x) :
    sum = 0

    try :
        for i in range(n) : 
            sum = sum + ((-1) ** i * x ** (2 * i)) / factorial(2 * i)

        return float(sum)
    except OverflowError as exception :
        # print('Its an Overflow error, please enter smaller degree.')

        return float(sum)


# Initialize

PI = math.pi
end_point_times = 500
machine_epsilon = countMachineEpsilon()

print(f"We found that the epsilon of your machine is {machine_epsilon}.\n")

input_degree = input("Please enter the degree you want to count: ")
input_degree = int(input_degree)
degree_to_radian = input_degree * PI / 180
true_value = math.cos(degree_to_radian)

input_significant_figures = input("Please enter the significant figures: ")
input_significant_figures = int(input_significant_figures)
error_criterion = countErrorCriterion(input_significant_figures)


print(f"\nThe degree you have entered -> {input_degree}°.")
print(f"And turn in radian -> {degree_to_radian}.")
print(f"The stopping criterion -> {error_criterion} %.")
print(f"The end-point of this program -> {end_point_times} times.")
print(f"True value of cos({degree_to_radian}) -> {true_value}.")


# main

is_start = str(input("\nReady to show the result?\n(a) Yes. (b) No.\n"))

print()
if (is_start == 'a') :
    print("Let's started to run the program.\n")
elif (is_start == 'b') :
    print("We still need to run the program.\n")
else :
    print("Wrong syntax, please type \"a\" or \"b\". However, let's started.\n")

loop_count = 0
current_approximate = 0.0
previous_approximate = 0.0


while True :

    if (loop_count == end_point_times) :
        print(f"Total use: {loop_count}. The runtimes are up to the limit!!!")
        print("We recommend you enter the smaller degree or significant figures!!!")

        break

    previous_approximate = current_approximate
    current_value = cosineTylorPolynomial(loop_count, degree_to_radian)
    current_approximate = current_value
    approximate_estimate_error = countApproximateEstimateError(current_approximate, previous_approximate)
    percent_relative_error = countPercentRelativeError(true_value, current_value)

    if (approximate_estimate_error < error_criterion) :
        loop_count += 1

        print(f"Total use {loop_count} times to get the result we want!")
        print(f"The current value: {current_value}.")
        print(f"The approximate estimate error: {approximate_estimate_error} %.")
        print(f"The percent relative error: {percent_relative_error} %.\n")
        print(f"Here is the error that we accept!!!")
        
        break
    
    loop_count += 1