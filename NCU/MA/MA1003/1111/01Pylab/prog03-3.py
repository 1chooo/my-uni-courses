import pylab

def f(x) :
    return pylab.sin(x) + pylab.cos(2 * x)

pi = pylab.pi
a, b, n = 0, 2 * pi, 100

xs = pylab.linspace(a, b, n)
ys = f(xs)

pylab.figure(facecolor='w')
pylab.plot(xs, ys)
pylab.grid()
pylab.xlabel("X")
pylab.ylabel("Y")
pylab.title("sin(x) + cos(2x)")
pylab.savefig("./img/plotFunction.png")

pylab.show()