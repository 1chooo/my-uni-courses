import math
from Error import Error
from sympy import *


# Show the Assignment required

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


def tylorPolynomial(n, x) :     # Build cosine tylor polynomial
    sum = 0

    for i in range(n) : 
        sum = sum + ((-1) ** i * x ** (2 * i)) / Error.factorial(2 * i)

    return float(sum)


# Announce the variable.

PI = math.pi
n = 5
errorCriterion = Error.countErrorCriterion(n)
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
    approximateEstimateError = Error.countApproximateEstimateError(currentApproximate, previousApproximate)
    percentRelativeError = Error.countPercentRelativeError(trueValue, currentValue)

    if (approximateEstimateError < errorCriterion) :
        loopCount += 1

        print(f"Times: {loopCount}, \ncurrent value: {currentValue}, \tapproximate estimate error: {approximateEstimateError} \tpercent relative error: {percentRelativeError}%.\n")
        print(f"Here is the error that we accept!!!")
        print(f"Total use {loopCount} times to get the result we want!")

        break
    else :
        loopCount += 1

    print(f"Times: {loopCount}, \ncurrent value: {currentValue}, \tapproximate estimate error: {approximateEstimateError} \tpercent relative error: {percentRelativeError}%.")