import pylab
import numpy as np

a, b, n = 0, 100*np.pi, 10000
angs = np.linspace(a, b, n)
rs = (np.cos(np.pi * angs))

pylab.polar(angs, rs, lw = 1, color = 'b')
pylab.title("graph of cos(pi x) for x in [0, 100pi] using 10000 points", color = 'r')

pylab.show()