# -*- coding: utf-8 -*-


import numpy as np
from math import *
from random import *
import matplotlib.pyplot as plt

erase = '\x1b[1A\x1b[2K'

def f(x):
    return np.sin(x)

def g(x):
    return np.sin(x) * np.cos(5*x)

def O(x):
    return 0*x

min_x, max_x = 0, 2*np.pi
min_y, max_y = -1, 1
Number_of_total_point = 100000
print_count = int(Number_of_total_point/1000)

count_fx, count_all = 0, 0
Area = fabs((max_x - min_x)*(max_y - min_y))
print_count = print_count if(print_count > 0) else 1

linspace_x = np.linspace(min_x, max_x, 1000)
list_fox_x, list_fox_y = [], []
list_out_x, list_out_y = [], []

print('Start : ')

for i in range(Number_of_total_point):
    if(i%print_count == 0):
        progress_bar = int((i+1)/Number_of_total_point*10)
        #print(erase + '\x1b[92m' + 'Start : ' + str(round(i/Number_of_total_point*100, 1)) + '%  -> ' + '▉'*progress_bar + '_'*(10-progress_bar))
    px, py = uniform(min_x, max_x), uniform(min_y, max_y)
    f_of_px = f(px)
    g_of_px = g(px)
    if( f_of_px*py >= 0 and fabs(f_of_px) >= fabs(py) and f_of_px != 0 and g_of_px*py >= 0 and fabs(g(px)) >= fabs(py) ):
        list_fox_x.append(px)
        list_fox_y.append(py)
    else:
        list_out_x.append(px)
        list_out_y.append(py)
print(erase + 'Start : ' + '100%  -> ', '▉'*int((i+1)/Number_of_total_point*10))
print('The area of f(x) : ' + str(len(list_fox_x)/(len(list_out_x)+len(list_fox_x))*Area) )

# If there are too many points in the list, you would spend a lot of time waiting for the plot.
if(Number_of_total_point <= 150000):
    # Decide the size of the figure
    fg_size_max = 15 if((max_x - min_x)/(max_y - min_y) > 1.6) else 7.5
    fg_size_x = fg_size_max if((max_x - min_x)/(max_y - min_y) > 1.6) else fg_size_max*(max_x - min_x)/(max_y - min_y)
    fg_size_y = fg_size_max if((max_x - min_x)/(max_y - min_y) < 1.6) else fg_size_max*(max_y - min_y)/(max_x - min_x)
    # Set what kind of fugure we want and plot the figure.
    plt.figure(figsize = (fg_size_x, fg_size_y))
    plt.scatter(list_out_x, list_out_y, color = (1, 0, 0), marker = '.', s = 0.1 )
    plt.scatter(list_fox_x, list_fox_y, color = (0, 1, 0), marker = '.', s = 0.1 )
    plt.plot(linspace_x, f(linspace_x), color = (0, 0, 1), linestyle = "--" )
    plt.plot(linspace_x, O(linspace_x), color = (0, 0, 1) )
    plt.plot(linspace_x, g(linspace_x), color = (0, 0, 1) )
    plt.xlim( min_x, max_x )
    plt.ylim( min_y, max_y )
    plt.tight_layout()
    plt.show()
