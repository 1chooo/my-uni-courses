import numpy as np
import math

pi = math.pi

def f(x):
    return np.cos(x)

#richardson extrapolation ch23
def D(x, h):
    x_i_inc = x + h
    x_i_dec = x - h
    d = (f(x_i_inc) - f(x_i_dec)) / (2*h)
    return d

def Richardson(h_1, h_2, x):
    ric = (4/3) * D(x, h_2) - (1/3) * D(x, h_1)
    return ric

print('ans:', Richardson(pi/3, pi/6, pi/4))
