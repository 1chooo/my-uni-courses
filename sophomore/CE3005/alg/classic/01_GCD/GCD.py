def GCD(m, n) :
    r = m % n

    while (r != 0) :
        m = n
        n = r
        r = m % n

    return n
