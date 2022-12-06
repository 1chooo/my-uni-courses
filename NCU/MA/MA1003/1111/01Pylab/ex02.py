import pylab

def f(x) :
    return pylab.cos(x) ** 2 / pylab.sqrt(pylab.maximum(1, 2 * x - 1))

PI = pylab.pi
a, b, n = 0, 10 * PI, 100
xs = pylab.linspace(a, b, n)

pylab.figure(facecolor='w')
pylab.plot(xs, f(xs), color = "purple")
pylab.grid()
pylab.xlabel("X")
pylab.ylabel("Y")
pylab.title("f(x)=cos(x)^2/sqrt(max(1, 2x-1))", fontsize = 8)
pylab.savefig("./img/ex02.png")

pylab.show()