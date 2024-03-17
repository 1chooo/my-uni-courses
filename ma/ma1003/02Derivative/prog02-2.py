import pylab

def f(x) :
    return pylab.sin(x) + pylab.cos(2 * x)

def df(x) :
    return pylab.cos(x) - 2 * pylab.sin(2 * x)

def df2(x, h) :
    return (f(x + h) - f(x)) / h

PI = pylab.pi
a, b, n = 0, 2 * PI, 50
h = (b - a) / (n - 1)
xs = pylab.linspace(a, b, n)
ys = f(xs)
ys1 = df(xs)
ys2 = df2(xs, h)

pylab.figure(facecolor="w")
pylab.plot(xs, ys, label = "f(x)")
pylab.plot(xs, ys1, label = "exact f'(x)")
pylab.plot(xs, ys2, label = "computed f'(x)")
pylab.grid()
pylab.xlabel("X")
pylab.ylabel("Y")
pylab.title("sin(x)+cos(2x) and derivatives")
pylab.legend(loc = 2)
pylab.savefig("./img/derivative.png")

pylab.show()