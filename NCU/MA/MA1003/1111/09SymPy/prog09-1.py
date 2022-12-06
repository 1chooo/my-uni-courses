from sympy import *

init_printing()
x = var("x")

fn = x + floor(x)

for i in range(2) :
    y1 = Limit(fn, x, i, '-')
    y2 = Limit(fn, x, i, '+')
    y3 = Limit(fn, x, i + Rational(1, 2))

    pprint(y1)
    print('=', y1.doit(), end = "\n\n")

    pprint(y2)
    print('=', y2.doit(), end = "\n\n")

    pprint(y3)
    print('=', y3.doit(), end = "\n\n")