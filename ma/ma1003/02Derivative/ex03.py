import pylab

def g(t) :
    if ((t % pylab.pi) <= (1 / 2 * pylab.pi)) :
        return 1
    return -1

def h(t) :
    return 1.2732 * pylab.sin(2 * t) + 0.4244 * pylab.sin(6 * t) + 0.25465 * pylab.sin(10 * t) + 0.18189 * pylab.sin(14 * t) + 0.14147 * pylab.sin(18 * t)

def dh(t, h) :
    return (h(t + h) - h(t)) / h

a, b, n = -3.1, 3.1, 500
xs = pylab.linspace(a, b, n)
ys = h(xs)
ys_2 = g(xs)

pylab.figure(facecolor="w")
pylab.plot(xs, ys)
pylab.plot(xs, ys_2)
pylab.grid()
pylab.xlabel("X")
pylab.ylabel("Y")
pylab.title("f(x) = sqrt(2sin(x)+cos(2x)+3/(x+1)) and computed derivative", fontsize = 8)
pylab.savefig("./img/ex03.png")

pylab.show()