from mailbox import linesep
import pylab

def f(x) :
    return pylab.sin(x) + pylab.cos(2 * x)

a, b, n = 0, 2 * pylab.pi, 100

xs = pylab.linspace(a, b, n)

pylab.plot(xs, f(xs))
pylab.grid()
pylab.savefig("./img/sineFunction.png")
pylab.show()