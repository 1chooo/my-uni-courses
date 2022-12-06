from turtle import color
import pylab

def f(x) :
    return pylab.maximum(abs(x * pylab.sin(x)), abs(x * pylab.cos(x)))

def g(x) :
    return pylab.minimum(abs(x * pylab.sin(x)), abs(x * pylab.cos(x)))

PI = pylab.pi
a, b, n = -2 * PI, 2 * PI, 10000
xs = pylab.linspace(a, b, n)

pylab.figure(facecolor='w')
pylab.plot(xs, f(xs), color = "b")
pylab.plot(xs, g(xs), color = "g")
pylab.grid()
pylab.xlabel("X")
pylab.ylabel("Y")
pylab.xlim(-8, 7)
pylab.ylim(0, 7)
pylab.title("f(x)=max(abs(x sin(x)), abs(x cos(x))), g(x)=min(abs(x sin(x)), abs(x cos(x)))", fontsize = 8)
pylab.savefig("./img/ex01.png")

pylab.show()