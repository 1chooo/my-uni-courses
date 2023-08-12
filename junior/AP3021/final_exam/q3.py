# %% [markdown]
# # 2023 Final Exam 
# 
# ### Course: AP3021
# 
# ## Question 3

# %%
import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np

# %% [markdown]
# ### 讀資料

# %%
mat_contents = sio.loadmat("cceqs.mat")
sorted(mat_contents.keys())
Tc = mat_contents['Tc'][0]
e = mat_contents['e'][0]

print(len(Tc))
print(Tc)

print()

print(len(e))
print(e)

# %% [markdown]
# ### 確認資料

# %%
plt.scatter(Tc,e)
plt.title("Vapor Pressure vs Temperature")
plt.ylabel("Vapor Pressure (Pa)")
plt.xlabel("Temperature (degree Celsius)")

plt.show()

# %% [markdown]
# #### a. Please construct the C-C equation using the LINEAR regression

# %% [markdown]
# ### Define the LINEAR regression

# %%
def regression(x, y, n):

    sum_x = 0   # the sum of the x
    sum_y = 0   # the sum of the y

    sum_xy = 0  # the sum of the x * y
    sum_x2 = 0  # the sum of the x ^ 2

    st = 0      
    sr = 0      

    for i in range(0, n):
        sum_x += x[i]
        sum_y += y[i]

        sum_xy += x[i] * y[i]
        sum_x2 += x[i] * x[i]

    x_mean = sum_x / n
    y_mean = sum_y / n

    a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
    a0 = y_mean - a1 * x_mean

    for i in range(0, n):
        st += (y[i] - y_mean) ** 2
        sr += (y[i] - a0 - a1 * x[i]) ** 2

    std_estimate_error = (sr - (n - 2)) ** 0.5
    r2 = (st - sr) / st
    r = ((st - sr) / st) ** 0.5

    return a0, a1, std_estimate_error, r2, r

# %% [markdown]
# ### Data with the LINEAR regression

# %%
data_size = len(Tc)
a0, a1, std_estimate_error, r2, r = regression(Tc, e, data_size)

print("After the LINEAR regression:\n")
print("a0:                              ", a0)
print("a1:                              ", a1)
print("std_estimate_error:              ", std_estimate_error)
print("Coefficient of the determination:", r2)
print("Coefficient of the correlation:  ", r)

# %% [markdown]
# ### Plot the LINEAR regression to the figure.

# %%
xs = np.arange(-30, 35, 0.1)
ys = a1 * xs + a0
plt.plot(xs, ys, 'r')
plt.scatter(Tc,e)
plt.title("Vapor Pressure vs Temperature")
plt.ylabel("Vapor Pressure (Pa)")
plt.xlabel("Temperature (degree Celsius)")
plt.legend(["regression:\ny = 879.9865701296675x + 41.10433052361058", "input data"])
plt.grid()

plt.show()

# %% [markdown]
# #### b. Please determine the goodness of fitting

# %% [markdown]
# ### Turn to the $ln$

# %%



