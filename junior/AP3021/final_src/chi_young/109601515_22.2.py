def f(x):
    return ((2*x) + (3/x))**2

# Romberg line:5~40
def TrapEq(a, b, n):
    h = (b - a) / n
    x = a
    sum_tra = f(x)
    for i in range(1, n):
        x = x + h
        sum_tra = sum_tra + 2 * f(x)

    sum_tra = sum_tra + f(b)
    Trap = (b - a) * sum_tra / (2 * n)
    return Trap

def I(j, k, a, b):
    if k == 1:
        n = 2 ** (j - 1)
        return TrapEq(a, b, n)
    else:
        i_jk = ((4**(k-1)) * I(j+1, k-1, a, b) - I(j, k-1, a, b)) / ((4**(k-1)) - 1)
        return i_jk

def Romberg(a, b, es):
    i_ter = 0
    while True:
        i_ter = i_ter + 1

        for k in range(2, i_ter + 2):
            j = 2 + i_ter - k
            #print(I(j, k, a, b))

        ea = abs((I(1, i_ter + 1, a, b) - I(2, i_ter, a, b)) / I(1, i_ter + 1, a, b)) * 100
        #print('ea = ', ea)
        if ea < es:
            #print('iter = ', i_ter)
            break

    return I(1, i_ter + 1, a, b)

print('ans', Romberg(1, 2, 0.05))
