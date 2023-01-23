# %% [markdown]
# # Assignment6
# 
# Course: AP3021
# 
# Student Number: 109601003
# 
# Name: 林群賀

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

# %% [markdown]
# ## Q6-2
# 
# ### 1. Determine the condition number for the following system using the row-sum norm. Do not normalize the system.

# %%
a = np.array([[ 1,  4,  9, 16, 25],
              [ 4,  9, 16, 25, 36],
              [ 9, 16, 25, 36, 49],
              [16, 25, 36, 49, 64],
              [25, 36, 49, 64, 81]])
a_determinant = np.linalg.det(a)

print("Condition number of A:", np.linalg.cond(a, p=None))

# print('determinant of A =', a_determine)

# %% [markdown]
# ### 2. Repeat (a) but scale the matrix by making the max element in each row to 1.

# %%
a = np.float32([[ 1,  4,  9, 16, 25],
              [ 4,  9, 16, 25, 36],
              [ 9, 16, 25, 36, 49],
              [16, 25, 36, 49, 64],
              [25, 36, 49, 64, 81]])

for i in range(0, 5) :
    for j in range(0, 5) :
        a[i][j] = float(a[i][j] / a[i][4])
        # print(a[i][j])
        
print("Making the max element in each row to 1:\n")
print(a)

# %% [markdown]
# ### 3. 想想看，由condition number可知，這是一個什麼樣的矩陣呢?
# 
# ![6.2-3](./imgs/6.2-3.jpg)

# %% [markdown]
# ## Q6-3

# %%
a = np.array([[0, 1,  0,  0],
              [0, 0,  2,  1],
              [1, 1,  0,  0],
              [1, 1, -1, -1]])
b = np.array([[1],[1],[4],[0]])

inverse_a = np.linalg.inv(a)
print(inverse_a.dot(b))

# %% [markdown]
# ## Q6-4
# 
# ### LU decomposition.

# %%
a = np.array([[ 6,  15,  55],
              [15,  55, 225],
              [55, 225, 979]])
b = np.array([[152.6],
              [585.6],
              [2488.8]])


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

# %% [markdown]
# ## Q6-5

# %%
a = np.array([[ 0.8, -0.4,  0.0],
              [-0.4,  0.8, -0.4],
              [ 0.0, -0.4,  0.8]])
b = np.array([[ 41],
              [ 25],
              [105]])

x1 = 0
x2 = 1
x3 = 0
count = 0
c = 1.2

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

# %% [markdown]
# ## Q6-6
# 
# ### 1. without relaxation.

# %%
a = np.array([[ 2.0, -6.0, -1.0],
              [-3.0, -1.0,  7.0],
              [-8.0,  1.0, -2.0]])
b = np.array([[-38.0],
              [-34.0],
              [-20.0]])

def pivot(a, b):  

    p = np.array((a), float)
    q = np.array((b), float)
    n = len(q)

    for i in range(0, n - 1):

        if abs(p[i, 1]) == 0:
            for k in range(i + 1, n):
                if abs((p[k, i])) > abs(p[i, i]):
                    p[[i, k]] = p[[k, i]]
                    q[[i, k]] = q[[k, i]]

                    break

        for j in range(i + 1, n):
            f = p[j][i] / p[i][i]
            p[j, :] = p[j, :] - f * p[i, :]
            q[j] = q[j] -f * q[i]

    return p,q


a, b = pivot(a, b)
x1 = 1
x2 = 1
x3 = 1
count = 0
es = 0.05

while True:

    xold1 = x1
    xold2 = x2
    xold3 = x3
    count += 1
    x1 = ((b[0][0]) - (a[0][1]) * xold2 - (a[0][2]) * xold3) / a[0][0]
    x2 = ((b[1][0]) - (a[1][0]) * xold1 - (a[1][2]) * xold3) / a[1][1]
    x3 = ((b[2][0]) - (a[2][0]) * xold1 - (a[2][1]) * xold2) / a[2][2]

    if (((x1 - xold1) / x1) < es) and \
             ((x2-xold2)/x2 < es) and \
             ((x3-xold3)/x3 < es) :
        break


print('without relaxation')
print('x1 =', x1)
print('x2 =', x2)
print('x3 =', x3)
print()
print('Total used', count, "times.")

# %% [markdown]
# ### 2. with relaxation.
# 

# %%
a, b = pivot(a, b)
x1 = 1
x2 = 1
x3 = 1
count = 0
c = 1.2
es = 0.05

while True:
    xold1 = x1
    xold2 = x2
    xold3 = x3
    count += 1
    x1 = ((b[0][0]) - (a[0][1]) * xold2 - (a[0][2]) * xold3) / a[0][0]
    x2 = ((b[1][0]) - (a[1][0]) * xold1 - (a[1][2]) * xold3) / a[1][1]
    x3 = ((b[2][0]) - (a[2][0]) * xold1 - (a[2][1]) * xold2) / a[2][2]
    x1 = c * x1 + (1 - c) * xold1
    x2 = c * x2 + (1 - c) * xold2
    x3 = c * x3 + (1 - c) * xold3

    if (((x1 - xold1) / x1) < es) and \
             ((x2-xold2)/x2 < es) and \
             ((x3-xold3)/x3 < es) :
        break
    

print('with relaxation')
print('x1=',x1)
print('x2=',x2)
print('x3=',x3)
print()
print('Total used', count, "times.")

# %% [markdown]
# ## Q6-7

# %%
a = np.array([[-4,  1,  1,  0],
              [ 1, -4,  0,  1],
              [ 1,  0, -4,  1],
              [ 0,  1,  1, -4]])
b = np.array([[-275],
              [-225],
              [ -75],
              [-25]])

x1 = 1
x2 = 1
x3 = 1
x4 = 1
count = 0

while True:
    xold1 = x1
    xold2 = x2
    xold3 = x3
    xold4 = x4
    count += 1
    es = 0.0005
    x1 = (b[0][0] - a[0][1] * xold2 - a[0][2] * xold3 - a[0][3] * xold4) / a[0][0]
    x2 = (b[1][0] - a[1][0] * xold1 - a[1][2] * xold3 - a[1][3] * xold4) / a[1][1]
    x3 = (b[2][0] - a[2][0] * xold1 - a[2][1] * xold2 - a[2][3] * xold4) / a[2][2]
    x4 = (b[3][0] - a[3][0] * xold1 - a[3][1] * xold2 - a[3][2] * xold3) / a[3][3]

    if (((x1 - xold1) / x1) < es) and \
             ((x2-xold2)/x2 < es) and \
             ((x3-xold3)/x3 < es) :
        break

print('t11 =', x1)
print('t12 =', x2)
print('t21 =', x3)
print('t22 =', x4)
print()
print('Total used', count, "times.")

# %% [markdown]
# ## Q6-8
# 
# ### 1. Solve with the optimal gradient steepest descent method
# 
# ![6.8-1](./imgs/6.8-1.jpg)
# ### 2. Solve with the Newton’s method
# ![6.8-2](./imgs/6.8-2.jpg)
# 

# %% [markdown]
# ## Q6-9
# 
# $f(x, y) =e^{−x^{2}y^{2}}+cos(𝑥) +cos(2𝑦)$
# 
# using the steepest ascend method.
# 
# $f(x_0, y_0) = (-1, -1)$
# 
# ![6.9](./imgs/6.9.jpg)

# %% [markdown]
# 


