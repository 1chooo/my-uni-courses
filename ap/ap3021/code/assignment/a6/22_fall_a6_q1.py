# %% [markdown]
# # [2022 Fall] Assignment6-1
# 
# > Course: AP3021

# %% [markdown]
# ## Q6-1
# 
# ### 1. Determine the matrix inverse.

# %%
import numpy as np

a = np.array([[15, -3, -1],
              [-3, 18, -6],
              [-4, -1, 12]])
b = np.array([[3300], 
              [1200], 
              [2400]])

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


def inverse(x):
    LU_L = L(x)
    LU_U = U(x)
    inv = np.array([[0., 0., 0.],
                    [0., 0., 0.],
                    [0., 0., 0.]])

    for i in range(0, 3):
        if i == 0:
            b_1 = 1
            b_2 = 0
            b_3 = 0
        elif i == 1:
            b_1 = 0
            b_2 = 1
            b_3 = 0
        elif i == 2:
            b_1 = 0
            b_2 = 0
            b_3 = 1
        
        d1 = b_1/LU_L[0][0]
        d2 = (b_2-LU_L[1][0]*d1)/LU_L[1][1]
        d3 = (b_3-LU_L[2][0]*d1-LU_L[2][1]*d2)/LU_L[2][2]
        x3 = d3/LU_U[2][2]
        x2 = (d2-LU_U[1][2]*x3)/LU_U[1][1]
        x1 = (d1-LU_U[0][2]*x3-LU_U[0][1]*x2)/LU_U[0][0]
        inv[0][i] = x1
        inv[1][i] = x2
        inv[2][i] = x3

    return inv

inverse_a = inverse(a)
print(inverse_a)

# %% [markdown]
# ### 2. Use the inverse to determine the solution.

# %%
x = np.dot(inverse_a, b)
print(x)

# %% [markdown]
# ### 3. How much the rate of mass input to reactor 3 must be increased to induce a 10g/m3 rise in the concentration of reactor 1?

# %%
x[0][0] = x[0][0] - 10 
b_new = np.dot(a, x)

print('the rate of mass input to reactor3=', b_new[2][0])

# %% [markdown]
# ### 4. How much will the concentration in reactor 3 be reduced if the rate of mass input to reactors 1 and 2 is reduced by 700 and 350 g/day, respectively?

# %%
print('initial concentration in reactor3 =', x[2][0])

for i in range(1, 4):
    b[0][0] = b[0][0] - 700
    b[1][0] = b[1][0] - 350
    x_new = np.dot(inverse_a, b)

    print('Day', i, ': the concentration in reactor3 =', x_new[2][0])


