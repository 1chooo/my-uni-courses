# %% [markdown]
# # [2022 Fall] Assignment7-2
# 
# > Course: AP3021

# %% [markdown]
# ## Q7-2

# %% [markdown]
# ### Fit an exponential model to the data. Plot the data and the equation on standard/semi-log graph. (Python+繪圖)

# %%
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.4, 0.8,  1.2,  1.6,    2,  2.3])
y = np.array([800, 980, 1500, 1945, 2900, 3600])
lnx = np.log(x)
lny = np.log(y)
a0 = 1
a1 = 1

space=np.linspace(0, 2.5) # line space

A = np.zeros((2, 2))
B = np.zeros(2)

# Construct Matrix for solution
n = np.size(lnx)
m = 1
A[0, 0] = np.size(x)
A[0, 1] = np.sum(x)
A[1, 0] = np.sum(x)
A[1, 1] = np.sum(x ** 2)
B[0] = np.sum(lny)
B[1] = np.sum(x * lny)

# Solve AX=B to know a0(X[0]), a1(X[1])
X = np.inner(np.linalg.inv(A), B)
print("Condition number: ", np.linalg.cond(A))

# Construct regression line
regress = X[1] * space + X[0]
exp_regress = np.exp(regress)

# calculate St, Sr, Syx(STD), R^2, R
St = np.sum((lny - np.mean(lny)) ** 2)
Sr = np.sum((lny - X[0] - X[1] * x) ** 2)
Syx = np.sqrt(Sr / (n - (m + 1)))
r2 = (St - Sr) / St
r = np.sqrt(r2)

# R = (A[0, 0] * B[1] - A[0,1] * B[0]) / 
# (np.sqrt(A[0, 0] * A[1, 1] - A[0, 1] ** 2) *
# np.sqrt(A[0, 0] * np.sum(y ** 2) - B[0] ** 2))

print('Standard Deviation:', Syx)
print('Coefficient of determination:', r2)
print('Correlation Coefficient:', r)

plt.scatter(x, y, s=15)
plt.plot(space, exp_regress, 'r')
plt.title("Exponential Regression")
plt.legend(['Regression Line', 'Data Point'])
plt.grid()

plt.show()