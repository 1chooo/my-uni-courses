# %% [markdown]
# # [2022 Fall] Assignment6-5
# 
# > Course: AP3021

# %% [markdown]
# ## Q6-5

# %%
import numpy as np

# %%
a = np.array([
    [ 0.8, -0.4,  0.0],
    [-0.4,  0.8, -0.4],
    [ 0.0, -0.4,  0.8]]
)
b = np.array([
    [ 41],
    [ 25],
    [105]]
)

# %%
x1 = 0
x2 = 1
x3 = 0
count = 0
c = 1.2

# %%
while True:
    xold1 = x1
    xold2 = x2
    xold3 = x3
    es = 0.5 * 10 ** (-2)

    count += 1
    x1 = ((b[0][0]) - (a[0][1]) * x2 - (a[0][2]) * x3) / a[0][0]
    x1 = c * x1 + (1 - c) * xold1
    x2 = ((b[1][0]) - (a[1][0]) * x1 - (a[1][2]) * x3) / a[1][1]
    x2 = c * x2 + (1 - c) * xold2
    x3 = ((b[2][0]) - (a[2][0]) * x1 - (a[2][1]) * x2) / a[2][2]
    x3 = c * x3 + (1 - c) * xold3
    if ((x1 - xold1) / x1 < es) and \
           ((x2-xold2)/x2 < es) and \
           ((x3-xold3)/x3 < es) :
        break

print('x1 =', x1)
print('x2 =', x2)
print('x3 =', x3)
print()
print('Total used', count, "times.")


