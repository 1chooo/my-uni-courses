# -*-coding: utf-8 -*-

"""
Course: AP3021
Assignment: 1
Student id: 109601003
Name: 林群賀
"""

import math
from sympy import *


# The ask of the assignment 1:

x = Symbol("x")

k = Symbol("k")
two = Symbol("2")
four = Symbol("4")
six = Symbol("6")
twoK = Symbol("2k")
dot = Symbol("...")

print("The cos(0) tylor polynomial is: \n")
pprint(1 - x ** 2 / factorial(two) + x ** 4 / factorial(four) - x ** 6 / factorial(six) + dot + ((-1) ** k * x ** (twoK) / factorial(twoK)))
print()


# Build the factorial mechanism 

def factorial(n) :
    sum = 1

    for i in range(2, n + 1) :
        sum *= i

    return sum


#Build the error criterion : εs

def countErrorCriterion(n) :
    errorCriterion = (0.5 * 10 ** (2 - n)) * 100

    return errorCriterion


# Build the approximate estimate of the error : εa

def countApproximateEstimateError(currentApproximation, previousApproximation) :
    approximateError = currentApproximation - previousApproximation

    if currentApproximation == 0 :    # The first and second value of cosine tylor polynomial is 0.0 and 1.0; therefore we have to pass them.
        return 999
    else :
        approximateEstimateError = abs((approximateError / currentApproximation) * 100)

    return approximateEstimateError


# Build the percent relative error : εt

def countPercentRelativeError(trueValue, approximation) :
    trueError = trueValue - approximation
    percentRelativeError = (trueError / trueValue) * 100

    return percentRelativeError


# Build cosine tylor polynomial

def tylorPolynomial(n, x) :
    sum = 0

    for i in range(n) : 
        sum = sum + ((-1) ** i * x ** (2 * i)) / factorial(2 * i)

    return float(sum)


# Announce the variable.

PI = math.pi
n = 5
errorCriterion = countErrorCriterion(n)
loopCount = 0
currentApproximate = 0.0
previousApproximate = 0.0
trueValue = cos(2 * PI)
print(f"True value of cos(0): {trueValue}.")

# print((1.00000000000000 - 0.999978232974615 / 1.00000000000000) * 100)
print(f"The error criterion is: {errorCriterion}, and n = {n}.\n\nStart the estimate: \n")


# main

while True :
    previousApproximate = currentApproximate
    currentValue = tylorPolynomial(loopCount, 2 * PI)
    currentApproximate = currentValue
    approximateEstimateError = countApproximateEstimateError(currentApproximate, previousApproximate)
    percentRelativeError = countPercentRelativeError(trueValue, currentValue)

    if (approximateEstimateError < errorCriterion) :
        loopCount += 1

        print(f"Times: {loopCount}, \ncurrent value: {currentValue}, \tapproximate estimate error: {approximateEstimateError} \tpercent relative error: {percentRelativeError}%.\n")
        print(f"Here is the error that we accept!!!")
        print(f"Total use {loopCount} times to get the result we want!")

        break
    else :
        loopCount += 1

    print(f"Times: {loopCount}, \ncurrent value: {currentValue}, \tapproximate estimate error: {approximateEstimateError} \tpercent relative error: {percentRelativeError}%.")


""" The result printed in terminal: 

The cos(0) tylor polynomial is: 

    k  2k          6    4    2    
(-1) ⋅x           x    x    x     
───────── + ... - ── + ── - ── + 1
   2k!            6!   4!   2!    

True value of cos(0): 1.00000000000000.
The error criterion is: 0.05, and n = 5.

Start the estimate: 

Times: 1, 
current value: 0.0,     approximate estimate error: 999         percent relative error: 100.000000000000%.
Times: 2, 
current value: 1.0,     approximate estimate error: 100.0       percent relative error: 0%.
Times: 3, 
current value: -18.739208802178716,     approximate estimate error: 105.33640459720868  percent relative error: 1973.92088021787%.
Times: 4, 
current value: 46.200185220489566,      approximate estimate error: 140.560895400627    percent relative error: -4520.01852204896%.
Times: 5, 
current value: -39.25663198620415,      approximate estimate error: 217.6875928549489   percent relative error: 4025.66319862041%.
Times: 6, 
current value: 20.98800938567249,       approximate estimate error: 287.0431409898395   percent relative error: -1998.80093856725%.
Times: 7, 
current value: -5.438247397701897,      approximate estimate error: 485.9333320242407   percent relative error: 643.824739770190%.
Times: 8, 
current value: 2.465288973616568,       approximate estimate error: 320.59269545687425  percent relative error: -146.528897361657%.
Times: 9, 
current value: 0.7508982625278968,      approximate estimate error: 228.31198268020754  percent relative error: 24.9101737472103%.
Times: 10, 
current value: 1.0329042309836878,      approximate estimate error: 27.302237709610523  percent relative error: -3.29042309836878%.
Times: 11, 
current value: 0.9965213898411421,      approximate estimate error: 3.650984465907502   percent relative error: 0.347861015885786%.
Times: 12, 
current value: 1.000301224041822,       approximate estimate error: 0.3778695966608076  percent relative error: -0.0301224041822090%.
Times: 13, 
current value: 0.999978232974615,       approximate estimate error: 0.032299809791492   percent relative error: 0.00217670253850333%.

Here is the error that we accept!!!
Total use 13 times to get the result we want!
"""