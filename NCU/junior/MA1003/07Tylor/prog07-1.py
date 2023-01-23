from cProfile import label
import math
import numpy as np
import pylab

def factorial(n) :
    f = 1

    for i in range(2, n + 1) :
        f *= i

    return f

def tylorPolynomial(n, x) :
    sum = 0

    for i in range(n) :
        sum = sum + ((-1) ** i * x ** (2 * i)) / factorial(2 * i)

    return sum

a, b, m = 0, 2 * np.pi, 100
xs = np.linspace(a, b, m)
n = 10

for i in range(1, n + 1) :
    ys = tylorPolynomial(i, xs)
    pylab.plot(xs, ys, label = "P" + str(2 * (i - 1)))

pylab.plot(xs, np.cos(xs), label = "cos(x)")
pylab.title("Tylor polynomials with different orders of cos(x)", fontsize = 8)
pylab.legend()
pylab.grid()
pylab.xlabel("X")
pylab.ylabel("Y")
pylab.ylim(-2, 2)
pylab.xlim(0, 8)

pylab.savefig("./img/tylor-polynomials")
pylab.show()