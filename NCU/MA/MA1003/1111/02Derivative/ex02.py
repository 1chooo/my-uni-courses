import pylab

PI = pylab.pi

def f(x) :
    return pylab.sqrt((2 * pylab.sin(x) + pylab.cos(2 * x) + 3) / x + 1)

def df(x, h) :
    return (f(x + h) - f(x)) / h

a, b, n = 1, 20, 500
xs = pylab.linspace(a, b, n)
h = (b - a) / (n - 1)
ys = f(xs)

pylab.figure(facecolor="w")
pylab.plot(xs, ys, color = "blue")
pylab.plot(xs, df(xs, h), color = "green")
pylab.grid()
pylab.xlabel("X")
pylab.ylabel("Y")
pylab.title("f(x) = sqrt(2sin(x)+cos(2x)+3/(x+1)) and computed derivative", fontsize = 8)
pylab.savefig("./img/ex02.png")

pylab.show()