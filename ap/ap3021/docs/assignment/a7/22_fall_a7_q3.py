# %% [markdown]
# # [2022 Fall] Assignment7-3
# 
# > Course: AP3021

# %% [markdown]
# ## Q7-3

# %% [markdown]
# ### Use Newton’s interpolating polynomials of order 1 to 4 to get f(4). Choose your base points to attain good accuracy.(Python) (繪圖、值)

# %%
def f(m, n):
    
    a = (y[m] - y[n]) / (x[m] - x[n])

    return a

# %%
x = [1, 2,  3,  5,   7,   8]
y = [3, 6, 19, 99, 291, 444]
a = 4

ans = y[2] + (a - x[2]) * f(3, 2)

print("Newton's interpolating polynomials f(4) =", ans)