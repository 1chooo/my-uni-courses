# %% [markdown]
# # [2022 Fall] Assignment4-2
# 
# > Course: AP3021

# %%
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
import os

# %% [markdown]
# ## 4-2-1
# 
# How many bisection iterations would be required to determine temperature to an
# absolute error of 0.05°C? (𝑥𝑙 = 0°C, 𝑥𝑢 = 40°C)
# 
# ![plot](./src/imgs/A4_2_1.jpg)

# %% [markdown]
# ## 4-2-2
# 
# 延續(1). Bisection program. (𝑂𝑠𝑓 = 8, 10, 𝑎𝑛𝑑 12𝑚𝑔/𝐿) (Python) PS : 溫度請帶絕對溫標

# %%
def f(temperature, osf) :
    absolute_temperature = temperature + 273.15 # Ta

    ans = ((-8.621949 * 10 ** 11) / absolute_temperature ** 4) \
        + ((1.243800  * 10 ** 10) / absolute_temperature ** 3) \
        + ((-6.642308 * 10 **  7) / absolute_temperature ** 2) \
        + ((1.575701  * 10 **  5) / absolute_temperature)      \
        - 139.34411 - math.log(osf)
    
    return ans

# %%
def count_et(true_value, approximation) :
    true_error = true_value - approximation
    et = (true_error / true_value) * 100

    return et

# %%
def count_ea(new_x_root, old_x_root) :

    if (old_x_root == -1) : # jump out the first data.
        return 9999
    else :
        ea = abs((new_x_root - old_x_root) / new_x_root)
        ea = ea * 100   # turn into percent
        
        return ea

# %%
def count_iter_times(x_lowwer, x_upper, Ead) :
    iter_times = math.log(((x_upper - x_lowwer) / Ead), 2)

    return iter_times

# %%
def bisection(x_lowwer, x_upper, Ead, osf, iter_max, iter_count) :
    iter_times = count_iter_times(x_lowwer, x_upper, Ead)
    print("Iterator at least:", iter_times, "times.")
    x_root = -1
    
    while True :
        last_x_root = x_root
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

        # how to get the true_value?
        # true_value = 

        # et = (count_et(true_value, x_root))

        ea = count_ea(x_root, last_x_root)

        print("count:", iter_count, "root:", x_root, "ea", ea)
        # print(x_lowwer, x_upper)
        
        if iter_count >= iter_times or iter_count >= iter_max:
            temperature = x_root + 273.15
            
            print(f"if the os is {osf}\nI iterate {iter_count} times\nThe temperature is {temperature}K")
            return x_root

# %% [markdown]
# ### Osf = 8

# %%
x_lowwer = 0
x_upper = 40
Ead = 0.05
osf = 8
iter_max = 500
iter_count = 0

ans = bisection(x_lowwer, x_upper, Ead, osf, iter_max, iter_count)

# %% [markdown]
# ### Osf = 10

# %%
x_lowwer = 0
x_upper = 40
Ead = 0.05
osf = 10
iter_max = 500
iter_count = 0

print("Osf:", osf)
ans = bisection(x_lowwer, x_upper, Ead, osf, iter_max, iter_count)
print(ans)

# %% [markdown]
# ### Osf = 12

# %%
x_lowwer = 0
x_upper = 40
Ead = 0.05
osf = 12
iter_max = 500
iter_count = 0

print("Osf:", osf)
ans = bisection(x_lowwer, x_upper, Ead, osf, iter_max, iter_count)
print(ans)

# %%



