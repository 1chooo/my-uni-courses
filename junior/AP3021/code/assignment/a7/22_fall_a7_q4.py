# %% [markdown]
# # [2022 Fall] Assignment7-4
# 
# > Course: AP3021

# %% [markdown]
# ## Q7-4

# %% [markdown]
# ### Repeat Q18.6 using Lagrange polynomials of order 1 to 3. (Python) (繪圖、值) Interpret your results in word or print in code

# %%
def NewtInt(x, y, n, x_miss):

    fdd = np.zeros((n, n))
    fdd[0:n, 0] = y[0:n]

    for j in range(1, n, 1):
        for i in range(0, n-j, 1):
            fdd[i, j] = (fdd[i + 1, j-1] - fdd[i, j - 1]) / (x[i + j] - x[i])

    y_interp = y[0]
    xterm = 1.0

    for order in range(1, n):
        xterm = xterm * (x_miss - x[order - 1])
        y_interp = y_interp + fdd[0, order] * xterm

    return y_interp

# %%
import numpy as np

x = [1, 2,  3,  5,   7,   8]
y = [3, 6, 19, 99, 291, 444]
n = 3
x_miss = 4

ans_New = NewtInt(x, y, n, x_miss)

print("Newton's interpolating polynomials f(4) =", ans_New)