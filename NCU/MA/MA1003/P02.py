import pylab, numpy

def factorial(n) :
    
    f = 1
    for i in range(2, n+1) :
        f *= i
    return f

def taylor_poly(n, x) :
    
    s = 0
    for k in range(n) :
        s = s + ((-1) ** (k) * (x ** (2 * k)) / factorial(2 * k)) + ((-1) ** (k) * (x ** ((2 * k) + 1)) / factorial((2 * k) + 1))

    return s    

a, b, m = 0 , 3 * numpy.pi, 100
xs = numpy.linspace(a, b, m)

n = 10
for i in range(1, n+1) :
    ys = taylor_poly(i, xs)
    pylab.plot(xs, ys, label = "P" + str(2 * i - 1))

pylab.plot(xs,numpy.sin(xs) + numpy.cos(xs), label = "sin(x)+cos(x)")
pylab.title("HW1"
            "-"
            "Taylor polynomilas with different orders for sin(x)+cos(x)")
pylab.legend()
pylab.grid()
pylab.xlabel("X")
pylab.ylabel("Y")
pylab.ylim(-2, 2)
pylab.show()