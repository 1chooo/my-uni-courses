import pylab

PI = pylab.pi

def f(x) :
    return (2 + pylab.sin(x / PI)) / (2 - pylab.sin(x / PI))

def df(x, h) :
    return (f(x + h) - f(x)) / h

a, b, n = 0, 50, 100
xs = pylab.linspace(a, b, n)
h = (b - a) / (n - 1)
ys = f(xs)

pylab.figure(facecolor="w")
pylab.plot(xs, ys, color = "blue")
pylab.plot(xs, df(xs, h), color = "green")
pylab.grid()
pylab.xlabel("X")
pylab.ylabel("Y")
pylab.title("f(x) = (2 + sin(x/pi))/(2 - sin(x/pi)) and computed derivative", fontsize = 8)
pylab.savefig("./img/ex01.png")

pylab.show()