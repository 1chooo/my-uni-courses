# %% [markdown]
# # [2022 Fall] Assignment7-1
# 
# > Course: AP3021

# %% [markdown]
# ## Q7-1

# %% [markdown]
# ### a. Use least-squares regression to fit a straight line. Compute the standard error [Eq.17.9] of the estimate and the correlation coefficient. Assess the fit. (Python+繪圖)

# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,   2, 3, 4, 5, 6, 7,  8,  9])
y = np.array([1, 1.5, 2, 3, 4, 5, 8, 10, 13])

space = np.linspace(1, 10) # line space
A = np.zeros((2, 2))
B = np.zeros(2)

# Construct Matrix for solution
n = np.size(x)
m = 1
A[0, 0] = np.size(x)
A[0, 1] = np.sum(x)
A[1, 0] = np.sum(x)
A[1, 1] = np.sum(x ** 2)
B[0] = np.sum(y)
B[1] = np.sum(x * y)

# Solve AX=B to know a0(X[0]), a1(X[1])
X = np.inner(np.linalg.inv(A), B)
print("Condition number: ", np.linalg.cond(A))

# construct regression line
regress = X[1] * space + X[0]

St = np.sum((y - np.mean(y)) ** 2)
Sr = np.sum((y - X[0] - X[1] * x) ** 2)
Syx = np.sqrt(Sr / (n-(m+1)))
r2 = (St - Sr) / St
r = np.sqrt(r2)

print('Standard Deviation:', Syx)
print('Coefficient of determination:', r2)
print('Correlation Coefficient:', r)

plt.scatter(x, y, s=10)
plt.plot(space, regress, 'r')
plt.title("Linear Regression")
plt.legend(['Regression Line', 'Data Point'])
plt.grid()

plt.show()

# %% [markdown]
# ### b. Use polynomial regression to fit a parabola to the data. Compute the standard error and correlation coefficient. Compare with (a). (Python+繪圖)

# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,   2, 3, 4, 5, 6, 7,  8,  9])
y = np.array([1, 1.5, 2, 3, 4, 5, 8, 10, 13])

space = np.linspace(1, 10)

A = np.zeros((3, 3))
B = np.zeros(3)

# Construct Matrix for solution
n = np.size(x)
m = 2
A[0, 0] = np.size(x)
A[0, 1] = np.sum(x)
A[1, 0] = np.sum(x)
A[1, 1] = np.sum(x ** 2)
A[0, 2] = np.sum(x ** 2)
A[2, 0] = np.sum(x ** 2) 
A[1, 2] = np.sum(x ** 3)
A[2, 1] = np.sum(x ** 3)
A[2, 2] = np.sum(x ** 4)
B[0] = np.sum(y)
B[1] = np.sum(x * y)
B[2] = np.sum((x ** 2) * y)

# Solve AX=B to know a0(X[0]), a1(X[1])
X = np.inner(np.linalg.inv(A), B)
print("Condition number:", np.linalg.cond(A)) # Knowing the condition number

# construct regression line
regress = X[2] * (space ** 2) + X[1] * space + X[0]

# calculate St, Sr, Syx(STD), R^2, R
St = np.sum((y - np.mean(y)) ** 2)
Sr = np.sum((y - X[0] - X[1] * x - X[2] * (x ** 2)) ** 2)
Syx = np.sqrt(Sr / (n - (m + 1)))
r2 = (St - Sr) / St
r = np.sqrt(r2)

#print(A, B, X)
print('Standard Deviation:', Syx)
print('Coefficient of determination:', r2)
print('Correlation Coefficient:', r)

plt.scatter(x, y, s=15)
plt.plot(space, regress, 'r')
plt.title("Polynomial Regression")
plt.legend(['Regression Line', 'Data Point'])
plt.grid()

plt.show()