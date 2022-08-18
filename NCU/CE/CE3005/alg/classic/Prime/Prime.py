from math import sqrt


def primeCheck1(n) :
    for i in range(2, n) :
        if (n % i == 0) :
            return False
    
    return True


def primeCheck2(n) :
    for i in range(2, sqrt(n)) :
        if (n % i == 0) :
            return False

    return True