# %% [markdown]
# # [2022 Fall] Assignment1
# 
# > Course: AP3021

# %%
import math

# %% [markdown]
# Build the factorial mechanism 

# %%
def factorial(n) :
    sum = 1

    for i in range(2, n + 1) :
        sum *= i

    return sum

# %% [markdown]
# Build the error criterion : εs

# %%
def countErrorCriterion(n) :
    errorCriterion = (0.5 * 10 ** (2 - n)) * 100

    return errorCriterion

# %% [markdown]
# Build the approximate estimate of the error : εa

# %%
def countApproximateEstimateError(currentApproximation, previousApproximation) :
    approximateError = currentApproximation - previousApproximation

    if currentApproximation == 0 :    # The first and second value of cosine tylor polynomial is 0.0 and 1.0; therefore we have to pass them.
        return 999
    else :
        approximateEstimateError = abs((approximateError / currentApproximation) * 100)

    return approximateEstimateError

# %% [markdown]
# Build the percent relative error : εt

# %%
def countPercentRelativeError(trueValue, approximation) :
    trueError = trueValue - approximation
    percentRelativeError = (trueError / trueValue) * 100

    return percentRelativeError

# %% [markdown]
# Build cosine tylor polynomial

# %%
def tylorPolynomial(n, x) :
    sum = 0

    for i in range(n) : 
        sum = sum + ((-1) ** i * x ** (2 * i)) / factorial(2 * i)

    return float(sum)

# %% [markdown]
# Announce the variable.

# %%
def main():

    PI = math.pi
    n = 5
    errorCriterion = countErrorCriterion(n)
    loopCount = 0
    currentApproximate = 0.0
    previousApproximate = 0.0
    trueValue = math.cos(2 * PI)
    print(f"True value of cos(0): {trueValue}.")

    # print((1.00000000000000 - 0.999978232974615 / 1.00000000000000) * 100)
    print(f"The error criterion is: {errorCriterion}, and n = {n}.\n\nStart the estimate: \n")

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

# %%
if __name__ == '__main__':
    main()


