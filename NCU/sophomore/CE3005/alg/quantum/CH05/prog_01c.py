import itertools

def f1(x):
    return '1'
print(f1("000"), f1("001"), f1("010"), f1("011"), f1("100"), f1("101"), f1("110"), f1("111"))

def f2(x):
    if x[0] == '0':
        return '0'
    else:
        return '1'
print(f2("000"), f2("001"), f2("010"), f2("011"), f2("100"), f2("101"), f2("110"), f2("111")) 

def DJ_test(f, n):
    count0 = count1 = 0
    iter = itertools.product([0, 1], repeat = n)
    lst = [''.join(map(str, item)) for item in iter]
    for s in lst:
        if f(s) == '0':
            count0 += 1
        else:
            count1 += 1
        if count0 > 0 and count1 > 0:
            return True     # for balanced function
        elif count0 > 2 ** (n - 1) or count1 > 2 ** (n-1):
            return False    # dor constant function

print(DJ_test(f1, 3))
print(DJ_test(f2, 3))