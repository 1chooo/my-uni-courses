import pylab

def f(x) :
    return pylab.sqrt(pylab.cos(2 * x))

def df(x) :
    return (-pylab.tan(2 * x) * abs(pylab.cos(2 * x)) / pylab.sqrt(abs(pylab.cos(2 * x))))

def df2(x, h) :
    return (f(x + h) - f(x)) / h