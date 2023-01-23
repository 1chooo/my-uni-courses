import pylab

def f(x):
    return pylab.cos(x)**2 / pylab.sqrt(pylab.maximum(1, 2*x-1))
    
a, b, n = 0, 10*pylab.pi, 100
xs = pylab.linspace(a,b,n)
ys = f(xs)
pylab.plot(xs,ys)

pylab.show()