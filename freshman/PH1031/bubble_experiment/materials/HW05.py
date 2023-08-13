# -*- coding: utf-8 -*-

from matplotlib import pylab as p

"""
"""
def w(An,n,x):
    return An*p.cos(2*p.pi*n*x)

Y = 0
n = 9

while n<=15:
    An = 1/(abs(n-12)+1)
    x = p.linspace(-1.0,1.0,1000)
    y = w(An,n,x)
    p.plot(x,y)

    Y = Y+y
    n += 1
p.plot(X,Y,color='blue')

p.show()
