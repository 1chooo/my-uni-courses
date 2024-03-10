# %% [markdown]
# # [2022 Fall] Assignment6-2
# 
# > Course: AP3021

# %% [markdown]
# ## Q6-2
# 
# ### 1. Determine the condition number for the following system using the row-sum norm. Do not normalize the system.

# %%
import numpy as np

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


