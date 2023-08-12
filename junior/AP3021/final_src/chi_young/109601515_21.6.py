import math
import numpy as np
from scipy import integrate
e = math.exp(1)
def f(x):
    return (x**2) * (e**x)
def i_f(x):
    return (x**2) * (e**x) - 2 * x * (e ** x) + 2 * (e**x)
#trapezoidal
def trapm(n):
    h = float(3 / n)

    tra_sum = f(0.0)
    for i in range(1, n):
        tra_sum = tra_sum + 2 * f(i*h)

    tra_sum = tra_sum + f(3.0)
    trap = h * tra_sum / 2
    return trap
print('解析解：', i_f(3) - i_f(0))
print('trapezoidal:', trapm(4))
print()
err_trap = abs(((i_f(3) - i_f(0)) - trapm(4)) / (i_f(3) - i_f(0))) * 100
print('trapezoidal_error:', err_trap, '%')
#Simpson 1/3

def sime_13_m(n):
    sim_sum = f(0.0)
    h = float(3 / n)
    for i in range(1, n-1, 2):
        sim_sum = sim_sum + 4 * f(i*h) + 2 * f((i+1)*h)

    sim_sum = sim_sum + 4 * f((n-1)*h) + f(n*h)
    simp = h * sim_sum/ 3
    return simp
err_simp = abs(((i_f(3) - i_f(0)) - sime_13_m(4)) / (i_f(3) - i_f(0))) * 100
print('Simpson 1/3:', sime_13_m(4))

print('Simpson_error:', err_simp, '%')
