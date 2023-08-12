from sympy import *

init_printing()
var("x,y")

fn = x * y**2 * ln(x**2)

for i in range(1) :
    
    dfn1 = Derivative(fn, x, x, y)
    dfn2 = Derivative(fn, x, x, x)
    dfn3 = Derivative(fn, y, x, x)

    pprint(dfn1)
    print("=", dfn1.doit())
    print()

    pprint(dfn2)
    print("=", dfn2.doit())
    print()

    pprint(dfn3)
    print("=", dfn3.doit())
    print()