class Error :

    def factorial(n) :  # Build the factorial mechanism
        sum = 1

        for i in range(2, n + 1) :
            sum *= i

        return sum
        

    def countErrorCriterion(n) :    # Build the error criterion : εs
        errorCriterion = (0.5 * 10 ** (2 - n)) * 100

        return errorCriterion

    
    def countApproximateEstimateError(currentApproximation, previousApproximation) :    # Build the approximate estimate of the error : εa
        approximateError = currentApproximation - previousApproximation

        if currentApproximation == 0 :    # The first and second value of cosine tylor polynomial is 0.0 and 1.0; therefore we have to pass them.
            return 999
        else :
            approximateEstimateError = abs((approximateError / currentApproximation) * 100)

        return approximateEstimateError


    def countPercentRelativeError(trueValue, approximation) :   # Build the percent relative error : εt
        trueError = trueValue - approximation
        percentRelativeError = (trueError / trueValue) * 100

        return percentRelativeError