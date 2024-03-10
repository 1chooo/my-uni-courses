# %% [markdown]
# # [2022 Fall] Assignment7-6
# 
# > Course: AP3021

# %% [markdown]
# ## Q7-6

# %% [markdown]
# ### 1. Generate 8 equally-spaced points from f = sin2t from 0 to 2𝜋. Fit this data with a cubic spline.(Python+繪圖)

# %%
import numpy as np
import matplotlib.pyplot as plt

T = [     0,      8,    16,    24,    32,    40]
o = [14.621, 11.843, 9.870, 8.418, 7.305, 6.413]


PI = np.pi

def f(x):

    return (np.sin(x))**2


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

    x = [    PI / 4,     PI / 2, PI * 3 / 4, 
                 PI, PI * 5 / 4, PI * 6 / 4,
         PI * 7 / 4, PI * 2]

    for i in range(0, 8):
        y = [f(x[i])]

    plt.scatter(T, o, s=15)
    x_new = np.linspace(0, 2 * PI, 40)
    plt.title('Cubic spline')
    plt.plot(x_new, cubic_inter(x_new, x, y),'r')
    plt.legend(['Cubic spline', 'Data point'])
    plt.grid()
    plt.show()

    print('Cubic spline=',cubic_inter(x_new,x,y))

# %%


import numpy as np
import matplotlib.pyplot as plt

PI = np.pi

def f(x):
    return (np.sin(x))**2


if __name__ == '__main__':
    x = [PI / 4, PI / 2, PI * 3 / 4, PI, PI * 5 / 4, PI * 6 / 4, PI * 7 / 4, PI * 2]
    y = [f(val) for val in x]  # Collect all the data points

    plt.scatter(x, y, s=15)
    x_new = np.linspace(0, 2 * PI, 40)
    plt.title('Cubic spline')
    plt.plot(x_new, cubic_inter(x_new, x, y), 'r')
    plt.legend(['Cubic spline', 'Data point'])
    plt.grid()
    plt.show()

    print('Cubic spline=', cubic_inter(x_new, x, y))

