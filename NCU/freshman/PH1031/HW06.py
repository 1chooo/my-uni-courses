# -*- coding: utf-8 -*-

from matplotlib import pylab as p

"""
"""
Y = 0
n = 1
while n <= 9:
    x = p.linspace(-20.0,20.0,1000)
    y = p.sin(n*x)*1/n
    
    Y = Y+y
    
    if n == 3:
        p.plot(x,Y)
    if n == 5:
        p.plot(x,Y)
    if n == 9:
        p.plot(x,Y)
        
    n += 2
p.show()
