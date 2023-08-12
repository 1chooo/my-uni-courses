import pylab

def f(x) :
    return pylab.sin(x) / abs(2 * x)

PI = pylab.pi
a, b, n = -10 * PI, 10 * PI, 100
xs = pylab.linspace(a, b, n)

pylab.figure(facecolor='w')
pylab.plot(xs, f(xs))
pylab.grid()
pylab.xlabel("X")
pylab.ylabel("Y")
pylab.title("f(x)=sin(x)/|2x|", fontsize = 8)
pylab.savefig("./img/ex03.png")

pylab.show()