# %% [markdown]
# # [2022 Fall] Assignment6-3
# 
# > Course: AP3021

# %%
import numpy as np

# %%
a = np.array([[0, 1,  0,  0],
              [0, 0,  2,  1],
              [1, 1,  0,  0],
              [1, 1, -1, -1]])
b = np.array([[1],[1],[4],[0]])

inverse_a = np.linalg.inv(a)
print(inverse_a.dot(b))


