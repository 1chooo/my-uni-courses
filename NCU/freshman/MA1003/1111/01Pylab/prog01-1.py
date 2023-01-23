import pylab

def f(x) :
    return pylab.sin(2 * x) + pylab.sqrt(x)

def g(x) :
    return x ** 3 - 2 * x + pylab.cos(x / 3)

def h(x) :
    return pylab.sin(pylab.exp(x))

def s(x) :
    return pylab.log(x) + 2 * pylab.log10(x)

def t(x) :
    return pylab.sin(pylab.sqrt(abs(5 * x)))

def u(x) :
    return pylab.maximum(pylab.sin(x), pylab.cos(x) ** 2)

def v(x) :
    return pylab.minimum(pylab.sin(x), pylab.cos(2 * x))

a, b, n = 0, 10, 100
a, b, n = -pylab.pi, pylab.pi, 100

pi = pylab.pi
a, b, n = -pi, pi, 100

xs = pylab.linspace(a, b, n)
ys = f(xs)
ys = g(xs)

pylab.plot(xs, ys)
pylab.plot(xs, f(xs))

pylab.grid()
pylab.title("bar")
pylab.xlabel("X")
pylab.ylabel("Y")

pylab.show()