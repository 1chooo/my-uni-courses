# %% [markdown]
# # [2022 Fall] Assignment2-1
# 
# > Course: AP3021
# 
# ### Question: Evaluate the quantity $\sqrt{(c^2 + d)} -c$ to 4 correct significant figures, where c = 246886422468 and d = 13579.
# ### Answer: 

# %%
import math

c = 246886422468.0000
d = 13579.0000

def formula(c, d) :
    return math.sqrt(c ** 2 + d) - c


ans = formula(c, d)
print("%.4f" %(ans))

print(float((c * c + d)))

# %% [markdown]
# ![A2-1](./imgs/Picture1.jpg)

# %% [markdown]
# 


