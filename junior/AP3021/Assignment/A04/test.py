import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd

def f(temperature, osf) :
    absolute_temperature = temperature + 273.15 # Ta

    ans = ((-8.621949 * 10 ** 11) / absolute_temperature ** 4) \
        + ((1.243800  * 10 ** 10) / absolute_temperature ** 3) \
        + ((-6.642308 * 10 **  7) / absolute_temperature ** 2) \
        + ((1.575701  * 10 **  5) / absolute_temperature)      \
        - 139.34411 - math.log(osf)
    
    return ans

def count_et(true_iter_times, approximation) :
    true_error = true_iter_times - approximation
    et = (true_error / true_iter_times) * 100

    return et


def count_iter_times(x_lowwer, x_upper, Ead) :
    es = math.log(((x_upper - x_lowwer) / Ead), 2)

    return es

def bisection(x_lowwer, x_upper, Ead, osf, iter_max, iter_count) :
    iter_times = count_iter_times(x_lowwer, x_upper, Ead)
    print("Iterator at least:", iter_times)
    
    while True :
        x_root = (x_lowwer + x_upper) / 2
        iter_count += 1
        temp = f(x_lowwer, osf) * f(x_root, osf)
        # print(temp)

        if (temp < 0) :
            x_upper = x_root
            # print("here")
        elif(temp > 0) :
            x_lowwer = x_root
            # print("here2")
        else :
            return x_root

        # print("count:", iter_count, "root:", x_root)
        # print(x_lowwer, x_upper)
        
        if iter_count >= iter_times or iter_count >= iter_max:
            temperature = x_root + 273.15
            
            print(f"if the os is {osf}\nI iterate {iter_count} times\nThe relative percent error is \nThe temperature is {temperature}K")
            return x_root

x_lowwer = 0
x_upper = 40
Ead = 0.05
osf = 8
iter_max = 500
iter_count = 0

ans = bisection(x_lowwer, x_upper, Ead, osf, iter_max, iter_count)


def fix_point(x0, es, iter_max, ea_list, iter_count_list) :
    x_root = x0
    iter_count = 0

    while True :
        last_x_root = x_root
        x_root = g(last_x_root)
        iter_count += 1
        iter_count_list.append(iter_count)

        if (x_root != 0) :
            ea = abs((x_root - last_x_root) / x_root) * 100
            ea_list.append(ea)

        print("iter time:", iter_count, ",ea =", ea)
        if (ea < es or iter_count >= iter_max) :
            return x_root