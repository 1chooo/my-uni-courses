# %% [markdown]
# # [2022 Fall] Assignment6-6
# 
# > Course: AP3021

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


