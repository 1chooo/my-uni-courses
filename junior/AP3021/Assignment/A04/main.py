# %% [markdown]
# # Assignment4
# 
# Course: AP3021
# 
# Student Number: 109601003
# 
# Name: 林群賀

# %%
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
import os

# %% [markdown]
# ### 4-1.1:
# 
# Locate the first nontrivial root of $sin(x) = x^3$ where x is in radians. 
# 1. Graphical technique (Python)
# 2. Bisection program (𝑥𝑙 = 0.5, 𝑥𝑢 = 1, 𝑤h𝑒𝑛 𝜀𝑎 < 𝜀𝑠 = 2%) (Python)
# 

# %%
# plot y = sin(x) and y = x^3

x = np.linspace(-10, 10, 500)
y1 = np.sin(x)
y2 = x ** 3

plt.plot(x, y1)
plt.plot(x, y2)

plt.xlim(-10, 10)
plt.ylim(-10, 10)

plt.title("Technique of sin(x) = x^3")
plt.grid()
plt.legend(["sin(x)", "x^3"], loc ="lower right")
plt.axhline(y = 0, color='k', linestyle='-')

plt.savefig("./src/imgs/A4_1_a-1.png", dpi=300)

plt.show()

# %%
# plot y = sin(x) - x ^ 3
# set xl = 0.5; xu = 1.0

x = np.linspace(0.0, 1.0, 500)
y = np.sin(x) - x ** 3

plt.plot(x, y)

plt.xlim(0.49, 1.01)
plt.ylim(-0.25, 0.5)

plt.title("Technique of y = sin(x) - x^3")
plt.grid()
plt.legend(["sin(x) - x^3"], loc ="upper right")
plt.axhline(y = 0, color='k', linestyle='-')

plt.savefig("./src/imgs/A4_1_a-2.png", dpi=300)

plt.show()

# %%
# Bisection Program

def f(x) :
    ans = np.sin(x) - x ** 3
    return ans

def count_ea(new_x_root, old_x_root) :

    if (old_x_root == -1) : # jump out the first data.
        return 9999
    else :
        ea = abs((new_x_root - old_x_root) / new_x_root)
        ea = ea * 100   # turn into percent
    
    return ea

def bisection(x_lowwer, x_upper, es, x_root, iter_max) :
    iter_count = 0
    
    while True :
        last_x_root = x_root
        x_root = (x_lowwer + x_upper) / 2
        iter_count += 1
        ea = count_ea(x_root, last_x_root)
        temp = f(x_lowwer) * f(x_root)

        if (temp < 0) :
            x_upper = x_root
        elif(temp > 0) :
            x_lowwer = x_root
        else :
            ea = 0.0    
            # return x_root

        print("count:", iter_count, "root:", x_root, "ea:", ea)
        
        if ea < es or iter_count >= iter_max:
            return x_root

# %%
es = 2.0  # 2%
x_lowwer = 0.5
x_upper = 1.0
x_root = -1
iter_max = 500

ans = bisection(x_lowwer, x_upper, es, x_root, iter_max)

print("\nThe approximate ans:", ans)

# %% [markdown]
# ## 4-1.2
# 
# Also perform an error check by substituting your final answer into the original equation in 1-2 (calculate true error 可不用打程式)

# %%
# Also perform an error check by substituting your final answer into the original equation in (b) 

def count_true_error(true_value, approximation) :
    return true_value - approximation

def count_et(true_value, approximation) :
    true_error = true_value - approximation
    et = (true_error / true_value) * 100

    return et

true_value = 0.9286263  # calculator

et = count_et(true_value, ans)
print("True error:", et)

# %% [markdown]
# ### from the calculator
# 
# The root of $y = sin(x) - x^3$ is $−0.9286263, 0, 0.9286263$
# ![plot](./src/imgs/A4_1_b.png)
# 
# And from the previous conduction, true value is $0.9286263$ and the approximation is $0.7421875$.
# 
# Therefore we get the true percent error is $20.07683822868252\%$

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

def count_et(true_value, approximation) :
    true_error = true_value - approximation
    et = (true_error / true_value) * 100

    return et

def count_ea(new_x_root, old_x_root) :

    if (old_x_root == -1) : # jump out the first data.
        return 9999
    else :
        ea = abs((new_x_root - old_x_root) / new_x_root)
        ea = ea * 100   # turn into percent
        
        return ea


def count_iter_times(x_lowwer, x_upper, Ead) :
    iter_times = math.log(((x_upper - x_lowwer) / Ead), 2)

    return iter_times

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
# print(ans)

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
# print(ans)

# %% [markdown]
# ## 4-3-1
# 
# Develop a user-friendly subprogram for the modified false-position method based on Fig. 5.15. Test the program by determining the root of the function described in Example 5.6. Perform a number of runs until the true percent relative error falls below 0.01%. (Python)

# %%
def f(x) :
    ans = x ** 10 - 1

    return ans

def count_ea(new_x_root, old_x_root) :

    if (old_x_root == -1) : # jump out the first data.
        return 9999
    else :
        ea = abs((new_x_root - old_x_root) / new_x_root)
        ea = ea * 100   # turn into percent
    
    return ea

def count_et(true_value, approximation) :
    true_error = true_value - approximation
    et = abs((true_error / true_value) * 100)

    return et

def ModFalsePos(x_lowwer, x_upper, x_root, es, iter_max, iter_count_list, ea_list, et_list) :
    iter_count = 0
    iter_upper, iter_lowwer = 0, 0
    lowwer_value = f(x_lowwer)
    upper_value = f(x_upper)

    while True :
        last_x_root = x_root
        x_root = x_upper - upper_value * (x_lowwer - x_upper) / (lowwer_value - upper_value)
        root_value = f(x_root)

        iter_count += 1
        iter_count_list.append(iter_count)

        if (x_root != 0) :
            ea = count_ea(x_root, last_x_root)
            ea_list.append(ea)

        true_value = 1

        et = count_et(true_value, x_root)
        et_list.append(et)

        temp = lowwer_value * root_value

        if (temp < 0) :
            x_upper = x_root
            upper_value = f(x_upper)
            iter_upper = 0
            iter_lowwer += 1

            if (iter_lowwer >= 2) :
                lowwer_value /= 2
        elif (temp > 0) :
            x_lowwer = x_root
            lowwer_value = f(x_lowwer)
            iter_lowwer = 0
            iter_upper += 1

            if (iter_upper >= 2) :
                upper_value /= 2
        else :
            ea = 0.0
        
        print("count", iter_count, "ea", ea, "root", x_root)
        
        if (ea < es or iter_count >= iter_max) :
            return x_root

# %%
x_lowwer = 0
x_upper = 1.3
x_root = -1
true_percent_relative_error = 0.01 # 0.01%
iter_max = 500
iter_count_list = []
ea_list = []
et_list = []

print("\nthe approximate root:", ModFalsePos(x_lowwer, x_upper, x_root, true_percent_relative_error, iter_max, iter_count_list, ea_list, et_list))

# %% [markdown]
# ## 4-3-2
# 
# Plot the true and approximate percent relative errors versus number of iterations. (Python)

# %%
# plot ea and et

ea_list[0] = 99     #the first element is neglected.
x = iter_count_list
y1 = ea_list
y2 = et_list

plt.plot(x, y1)
plt.plot(x, y2)

plt.xlim(0.9, 13)
plt.ylim(0, 100)
plt.xlabel("iteration")
plt.ylabel("percent")

plt.title("et and ea versus number of the iterations")
plt.grid()
plt.legend(["ea", "et"], loc ="upper right")

plt.savefig("./src/imgs/A4_4_2.png", dpi=300)

plt.show()

# %% [markdown]
# ## 4-4-a
# 
# ### Fixed-point iteration 
# to determine a root of $f(x) = -0.9x^2 + 1.7x + 2.5$ using $x_0 = 5.0$. Perform the computation until 𝜀𝑎 is less than 𝜀𝑠 = 0.01%. Also perform an error check of your final answer(plot the 𝜀𝑎 as the iteration growing)
# 
# ![plot](./src/imgs/A4_4_a.jpg)

# %%
def g(x) :
    ans = math.sqrt((1.7 * x + 2.5) / 0.9)

    return ans

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

# %%
x0 = 5
es = 0.01
iter_max = 500
ea_list = []
iter_count_list = []

print("\nThe approximate ans:", fix_point(x0, es, iter_max, ea_list, iter_count_list))
# print(ea_list)
# print(iter_count)

# %%
# plot

x = iter_count_list
y = ea_list

plt.plot(x, y)

plt.xlim(0, 10)
plt.ylim(0, 50)

plt.title("Growing of ea by fixed point iteration")
plt.grid()
plt.legend(["ea"], loc ="upper right")

plt.savefig("./src/imgs/A4_4_a.png", dpi=300)

plt.show()

# %% [markdown]
# ### the Newton-Raphson method 
# to determine a root of $f(x) = -0.9x^2 + 1.7x + 2.5$ using $x_0 = 5.0$. Perform the computation until 𝜀𝑎 is less than 𝜀𝑠 = 0.01%. Also perform an error check of your final answer(plot the 𝜀𝑎 as the iteration growing)
# 
# ![plot](./src/imgs/A4_4_b.jpg)

# %%
def f(x) :
    ans = -0.9 * x ** 2 + 1.7 * x + 2.5

    return ans

def f_prime(x) :
    ans = -1.8 * x + 1.7

    return ans

def newton_raphson(x0, es, iter_max, ea_list, iter_count_list) :
    iter_count = 0

    while True :
        next_x = x0 - (f(x0) / f_prime(x0))
        x_root = next_x

        iter_count += 1
        iter_count_list.append(iter_count)

        ea = abs((x_root - x0) / x_root) * 100
        x0 = x_root
        ea_list.append(ea)
        

        print("iter time:", iter_count, ",ea =", ea)

        if (ea < es or iter_count >= iter_max) :
            return x_root

# %%
x0 = 5
es = 0.01
iter_max = 500
ea_list = []
iter_count_list = []

print("\nThe approximate ans:", newton_raphson(x0, es, iter_max, ea_list, iter_count_list))

# %%
# plot

x = iter_count_list
y = ea_list

plt.plot(x, y)

plt.xlim(0, 5)
plt.ylim(0, 50)

plt.title("Growing of ea by Newton Raphson")
plt.grid()
plt.legend(["ea"], loc ="upper right")

plt.savefig("./src/imgs/A4_4_b.png", dpi=300)

plt.show()

# %% [markdown]
# ## 4-5-1
# 
# Use the Newton-Raphson method to find the root of $f(x) = e^{-0.5x} (4 - x) - 2$
# 
# ![plot](./src/imgs/A4_5_1.jpg)

# %% [markdown]
# ## 4-5-2
# 
# Employ initial guesses of (a) 2, (b) 6, and (c) 8. Explain your results. (Python+解釋) Hint: Think about the problems of this method.

# %%
def f(x) :
    e = math.e
    ans = ((e ** (-0.5 * x)) * (4 - x)) - 2

    return ans

def f_prime(x) :
    e = math.e
    ans = (-0.5 * (e ** (-0.5 * x)) * (4 - x)) - (e ** (-0.5 * x))

    return ans

def newton_raphson(x0, es, iter_max) :
    iter_count = 0
    x_root = x0
    print("x0 =", x0)
    print()

    while True :
        last_x_root = x_root

        try :
            x_root = last_x_root - (f(x_root) / f_prime(x_root))
        except :
            print("total use", iter_count, "times.")
            return "Divergence"

        iter_count += 1
        iter_count_list.append(iter_count)
        if x_root != 0 :
            ea = abs((x_root - last_x_root) / x_root) * 100        

        print("iter time:", iter_count, ",ea =", ea, "root:", x_root)

        if (ea < es or iter_count >= iter_max) :
            print("total use", iter_count, "times.")
            return x_root

# %% [markdown]
# ### a. $x_0 = 2$

# %%
x0 = 2
es = 0.01
iter_max = 500

print("\nThe approximate ans:", newton_raphson(x0, es, iter_max))

# %% [markdown]
# ### b. $x_0 = 6$

# %%
x0 = 6
es = 0.01
iter_max = 500

print("\nThe approximate ans:", newton_raphson(x0, es, iter_max))

# %% [markdown]
# ### c. $x_0 = 8$

# %%
x0 = 8
es = 0.01
iter_max = 500

print("\nThe approximate ans:", newton_raphson(x0, es, iter_max))

# %% [markdown]
# ## 4-6-1
# 
# If R = 3 m, what depth must the tank be filled to so that it holds 30 𝑚3?
# 
# ![plot](./src//imgs/A4_6_1.jpg)
# 

# %% [markdown]
# ## 4-6-2
# 
# Newton-Raphson method (3 iterations; determine relative error after each iterations)(Python)
# 

# %%
def f(h, R, V) :
    PI = math.pi
    ans = PI * (h ** 2) * (((3 * R) - h) / 3) - V

    return ans

def f_prime(h, R) :
    PI = math.pi
    ans = (2 * PI * h * R) - (PI * (h ** 2))

    return ans

def newton_raphson(x0, es, iter_max, R, V) :
    iter_count = 0
    x_root = x0
    print("x0 =", x0)
    print()

    while True :
        last_x_root = x_root

        try :
            x_root = last_x_root - (f(x_root, R, V) / f_prime(x_root, R))
        except :
            print("total use", iter_count, "times.")
            return "Divergence"

        iter_count += 1
        iter_count_list.append(iter_count)
        if x_root != 0 :
            ea = abs((x_root - last_x_root) / x_root) * 100        

        print("iter time:", iter_count, ",ea =", ea, "root:", x_root)

        if (ea < es or iter_count >= iter_max) :
            print("total use", iter_count, "times.")
            return x_root

# %%
R = 3
V = 30
x0 = R
es = 0.01
iter_max = 3

print("\nThe constrains of h:", newton_raphson(x0, es, iter_max, R, V))

# %% [markdown]
# ## 4-6-3
# 
# What are the constraints of h?

# %%
print("\nThe constrains of h:", newton_raphson(x0, es, iter_max, R, V))

# %% [markdown]
# ### 4-7
# 
# Please read section 7.4 and describe the idea of Muller’s method.
# 
# 算是割線法的延伸，本想透過一直線通過函數到 x 軸的值來獲取數值解，不過 Muller's method 則做了修正，與割線法最大的不同就是透過「曲線」以曲線的性質變成透過第三個點來得到數值的分析解，作法則是用拋物線與 x 軸相交的點來得到數值解。

# %% [markdown]
# ### 4-8
# 
# Read chapter 7.2.2 and explain how to remove a found root of an nth-order polynomial.
# 
# 
# 在迭代數次之後常會發現得到相同的解，因此在我們要進行迭代數次的時候可以從小數點進行著手，以減輕 round-off error 為目標使得結果不會離我們預期的太過遙遠。
# 
# 使 round-off error 不會這麼影響我們的結果，便是要挑選好的估計值，有的時候我們需要從高次項著手，反之我們需要再低次項著手，在好的結果猜想中，所得到的結果可以使我們下次迭代中得到更好的結果，
# 
# 另一種方法是在 deflaction 將獲得的連續根視為良好的初步猜測。然後可以將每個估計值用做初始猜測，再運用 nondeflated polynomial 判定，不過要小心如果兩個 deflacted root 不夠準確以至於收斂至一個解的時候，可能會發生錯誤的誤差發生，此時便要去比對每一個 polished root。
# 
# ##### synthetic division
# ```
# r = a(n)
# a(n) = 0
# DOFOR i = n−1, 0, −1
#     s = a(i)
#     a(i) = r r=s+r*t
# END DO
# ```
# 
# 
# ##### Ploynomial deflaction
# ``` f90
# SUB poldiv(a, n, d, m, q, r) 
#     DOFOR j = 0, n
#         r(j) = a(j)
#         q(j) = 0 
#     END DO
#     DOFOR k = n−m, 0, −1 
#         q(k+1) = r(m+k) ∕ d(m) 
#         DOFOR j = m+k−1, k, −1
#             r(j) = r(j)−q(k+1) * d(j−k) 
#         END DO
#     END DO
#     DOFOR j = m, n
#         r(j) = 0 
#     END DO
#     n = n−m 
# END SUB
# ```

# %% [markdown]
# ### 4-9
# 
# Please write Python codes to determine the height of temperature inversion? (data is in the eeclass)

# %%
""" Data type:
stno: Observation's Number (Length: 6 digits)
yyyymmddhh: UTC Time, yyyy: year, mm: month, dd: day, hh: hour (Length: 11 digits)
Si: Significant Code (Length: 3 digits)
Press: Pressure (Uint: hpa, Length: 7 digits)
Heigh: Geopotential Height (Unit: gpm, Length: 6 digits)
Tx: Temperature (Unit: degrees Celsius, Length: 6 digits)
Td: Dew Point (Unit: degrees Celsius, Length: 6 digits)
Wd: Wind Direction (Unit: degrees 360, Length: 4 digits)
Ws: Wind Speed (Unit: m/s, Length: 6 digits)
RH: Relative Humidity (Unit: %, Length: 4 digits)
"""

# Fetch the local path to read the info of the file.
data_path = os.getcwd()
file = "/src/data/20210101_upair.txt"
file_path = f"{data_path}/{file}"


data = pd.read_csv(file_path, skiprows=13, sep="\s+")
data = data.replace(-0.99, 0)
data = data.replace(-9.99, 0)
data = data.replace(-1   , 0)
# stno yyyymmddhh Si  Press Heigh    Tx    Td  Wd    Ws  RH
data.columns = ["stno", "date", "Si", "press", "heigh", "Tx", "Td", "Wd", "Ws", "Rh"]

print(data)

# %%
# At first we observe the realtionship between height and temperature

plt.plot(data["Tx"], data["heigh"])

plt.xlabel("Temperature(˚c)")
plt.ylabel("Height(gpm)")
plt.title("the realtionship between height and temperature")

plt.grid()
plt.legend(["temperature"], loc ="upper right")
plt.savefig("src/imgs/A4_9_1.jpg", dpi = 300)

plt.show()

# %%
# the key point we need is height and the temperature

data_num = len(data)
inversion_happen = []
x = []
y = []

for i in range(0, data_num) :
    if (i == data_num - 1) :
        break

    if (data["Tx"][i] < data["Tx"][i + 1]) :
        inversion_happen.append(i)
        print("Height:", data["heigh"][i], "Temperature inversion:", data["Tx"][i])
        x.append(data["Tx"][i])
        y.append(data["heigh"][i])


plt.plot(data["Tx"], data["heigh"])
plt.scatter(x, y, c='red')

plt.xlabel("Temperature(˚c)")
plt.ylabel("Height(gpm)")
plt.title("the realtionship between height and temperature")

plt.grid()
plt.legend(["temperature", "temperature inversion"], loc ="upper right")
plt.savefig("src/imgs/A4_9_2.jpg", dpi = 300)

plt.show()


