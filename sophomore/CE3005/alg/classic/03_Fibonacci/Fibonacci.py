def fibonacci(n) :
    if (n == 1 or n == 2) :
        return 1
    else :
        a = 1
        b = 1

        for i in range(3, n + 1) :
            c = a + b
            a = b
            b = c
        
        return c


def recursiveFibonacci(n) :
    if (n == 1 or n == 2) :
        return 1
    else :
        a = recursiveFibonacci(n - 1)
        b = recursiveFibonacci(n - 2)

        return (a + b)