# %% [markdown]
# # [2022 Fall] Assignment7-5
# 
# > Course: AP3021

# %% [markdown]
# ## Q7-5 

# %% [markdown]
# ### 1. Using (a) Linear interpolation (b) Newton’s interpolating polynomial (c) Cubic splines to estimate o(27).
# 
# ### 2. Note that the exact result is 7.986 mg/L.

# %% [markdown]
# #### (a). Linear interpolation

# %%
import numpy as np
import matplotlib.pyplot as plt

T = [     0,      8,    16,    24,    32,    40]
o = [14.621, 11.843, 9.870, 8.418, 7.305, 6.413]
o27_1 = o[3] + (((o[4] - o[3]) / (T[4] - T[3])) * (27 - T[3]))
true_value = 7.986
ea = abs((true_value - o27_1) / true_value)

print('Linear interpolation o27 =', o27_1)
print('exact_result =', 7.986)
print('relative error =', ea)

plt.scatter(T, o, s=20)
plt.scatter(27, o27_1, s=20)
plt.plot(T, o)
plt.title("Linear interpolation")
plt.legend(['Linear interpolation', 'Data point', 'Linear interpolation value'])
plt.grid()

plt.show()

# %% [markdown]
# #### (b). Newton’s interpolating polynomial

# %%
def f(x, y):
    
    a = (o[x] - o[y]) / (T[x] - T[y])

    return a

def g(x, y, z):

    b = (f(x, y) - f(y, z)) / (T[x] - T[z])
    
    return b

def h(x, y, z, m):
    
    c = (g(x, y, z) - g(y, z, m)) / (T[x] - T[m])
    
    return c
    
def i(x, y, z, m, n):
    
    d = (h(x, y, z, m) - h(y, z, m, n)) / (T[x] - T[n])
    
    return d

# %%
import numpy as np
import matplotlib.pyplot as plt

T = [     0,      8,    16,    24,    32,    40]
o = [14.621, 11.843, 9.870, 8.418, 7.305, 6.413]
true_value = 7.986

o27_2 = o[0] \
    + (27 - T[0]) * f(1, 0) \
    + (27 - T[0]) * (27 - T[1]) * g(2, 1, 0) \
    + (27 - T[0]) * (27 - T[1]) * (27 - T[2]) * h(3, 2, 1, 0) \
    + (27 - T[0]) * (27 - T[1]) * (27 - T[2]) * (27 - T[3]) * i(4, 3, 2, 1, 0)

ea = abs((true_value - o27_2) / true_value)

print("Newton's interpolation o27=",o27_2)
print('exact_result=',7.986)
print('relative error=',ea)

# %% [markdown]
# #### (c) Cubic splines to estimate o(27).

# %%
import numpy as np
import matplotlib.pyplot as plt

T = [     0,      8,    16,    24,    32,    40]
o = [14.621, 11.843, 9.870, 8.418, 7.305, 6.413]
true_value = 7.986

def cubic_inter(x0, x, y):

    x = np.array(x)
    y = np.array(y)
    # remove non finite values
    # indexes = np.isfinite(x)
    # check if sorted
    if np.any(np.diff(x) < 0):
        indexes = np.argsort(x)
        x = x[indexes]
        y = y[indexes]

    size = len(x)
    xdiff = np.diff(x)
    ydiff = np.diff(y)

    # allocate buffer matrices
    Li = np.zeros(size)
    Li_1 = np.zeros(size - 1)
    z = np.zeros(size)

    # fill diagonals Li and Li - 1 and solve [L][y] = [B]
    Li[0] = np.sqrt(2 * xdiff[0])
    Li_1[0] = 0.0
    B0 = 0.0 # natural boundary
    z[0] = B0 / Li[0]

    for i in range(1, size-1, 1):
        Li_1[i] = xdiff[i - 1] / Li[i - 1]
        Li[i] = np.sqrt(2 * (xdiff[i - 1] + xdiff[i]) - Li_1[i - 1] * Li_1[i - 1])
        Bi = 6 * (ydiff[i] / xdiff[i] - ydiff[i - 1] / xdiff[i - 1])
        z[i] = (Bi - Li_1[i - 1] * z[i - 1]) / Li[i]

    i = size - 1
    Li_1[i - 1] = xdiff[-1] / Li[i - 1]
    Li[i] = np.sqrt(2*xdiff[-1] - Li_1[i - 1] * Li_1[i - 1])
    Bi = 0.0 # natural boundary
    z[i] = (Bi - Li_1[i - 1]*z[i - 1])/Li[i]

    # solve [L.T][x] = [y]
    i = size - 1
    z[i] = z[i] / Li[i]
    for i in range(size - 2, -1, -1):
        z[i] = (z[i] - Li_1[i - 1]*z[i+1])/Li[i]

    # find index
    index = x.searchsorted(x0)
    np.clip(index, 1, size - 1, index)

    xi1, xi0 = x[index], x[index - 1]
    yi1, yi0 = y[index], y[index - 1]
    zi1, zi0 = z[index], z[index - 1]
    hi1 = xi1 - xi0

    # calculate cubic
    f0 = zi0 / (6 * hi1) * (xi1 - x0) ** 3 \
        + zi1 / (6 * hi1) * (x0 - xi0) ** 3 \
        + (yi1 / hi1 - zi1 * hi1 / 6) * (x0 - xi0) \
        + (yi0 / hi1 - zi0 * hi1 / 6) * (xi1 - x0)
    
    return f0

# %%
if __name__ == '__main__':

    x_new = np.linspace(0, 40, 40)
    plt.scatter(T, o, s=15)
    plt.scatter(27, cubic_inter(x_new, T, o)[26], s=15)
    plt.title('Cubic spline')
    plt.plot(x_new, cubic_inter(x_new,T,o))
    plt.legend(['Cubic spline','Data point','Cubic spline value'])
    plt.grid()
    plt.show()

print('Cubic spline=', cubic_inter(x_new,T,o)[26])
print('exact_result=', 7.986)
ea = abs((true_value - cubic_inter(x_new,T,o)[26])/true_value)
print('relative error=',ea)