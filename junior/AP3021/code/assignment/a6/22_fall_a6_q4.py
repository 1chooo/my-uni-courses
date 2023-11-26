# %% [markdown]
# # [2022 Fall] Assignment6-4
# 
# > Course: AP3021

# %% [markdown]
# ## Q6-4
# 
# ### LU decomposition.

# %%
import numpy as np

# %%
a = np.array([
    [ 6,  15,  55],
    [15,  55, 225],
    [55, 225, 979]]
)
b = np.array([
    [152.6],
    [585.6],
    [2488.8]]
)

# %%
def L(x):

    f21 = x[1][0] / x[0][0]
    f31 = x[2][0] / x[0][0]
    x = np.array([[x[0][0], x[0][1], x[0][2]],
                  [x[1][0] - (x[0][0] * f21), x[1][1] - (x[0][1] * f21), x[1][2] - (x[0][2] * f21)],
                  [x[2][0] - (x[0][0] * f31), x[2][1] - (x[0][1] * f31), x[2][2] - (x[0][2] * f31)]])
    f32 = x[2][1] / x[1][1]

    return np.array([[  1,   0, 0],
                     [f21,   1, 0],
                     [f31, f32, 1]])

# %%
def U(x):

    a10 = x[1][0] / x[0][0]
    a20 = x[2][0] / x[0][0]
    x = np.array([[x[0][0], x[0][1], x[0][2]],
                  [x[1][0] - (x[0][0] * a10), x[1][1] - (x[0][1] * a10), x[1][2] - (x[0][2] * a10)],
                  [x[2][0] - (x[0][0] * a20), x[2][1] - (x[0][1] * a20), x[2][2] - (x[0][2] * a20)]])
    a21 = x[2][1] / x[1][1]
    x = np.array([[x[0][0], x[0][1], x[0][2]],
                  [x[1][0], x[1][1], x[1][2]],
                  [x[2][0], x[2][1] - (x[1][1] * a21), x[2][2] - (x[1][2] * a21)]])

    return x

# %%
d = np.dot(np.linalg.inv(L(a)), b)      # [L]{D} = {B}
x = np.dot(np.linalg.inv(U(a)), d)      # [U]{X} = {D}
print('After LU decomposition\n[L] =')
print(L(a))
print('[U] =')
print(U(a))
print('[A] =')
print(x)
print('a0 =', x[0], 'a1 =', x[1], 'a2 =', x[2])

# %% [markdown]
# ### Cholesky decomposition
# 

# %%
l11 = np.sqrt(a[0][0])
l21 = a[1][0] / l11
l22 = np.sqrt(a[1][1] - l21 ** 2)
l31 = a[2][0] / l11
l32 = (a[2][1] - l21 * l31) / l22
l33 = np.sqrt(a[2][2] - l31 ** 2 - l32 ** 2)
l = np.array([[l11,   0,   0],
              [l21, l22,   0],
              [l31, l32, l33]])
              
print('Cholesky decomposition')
print('[L]=')
print(l)


