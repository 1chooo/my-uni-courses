# %% [markdown]
# # [2022 Fall] Assignment6-7
# 
# > Course: AP3021

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


