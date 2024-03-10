# %% [markdown]
# # [2022 Fall] Assignment4-5
# 
# > Course: AP3021

# %% [markdown]
# ## 4-5-1
# 
# Use the Newton-Raphson method to find the root of $f(x) = e^{-0.5x} (4 - x) - 2$
# 
# ![plot](./src/imgs/A4_5_1.jpg)

# %% [markdown]
# ## 4-5-2
# 
# Employ initial guesses of (a) 2, (b) 6, and (c) 8. Explain your results. (Python+解釋) Hint: Think about the problems of this method.

# %%
import math

# %%
def f(x) :
    e = math.e
    ans = ((e ** (-0.5 * x)) * (4 - x)) - 2

    return ans

def f_prime(x) :
    e = math.e
    ans = (-0.5 * (e ** (-0.5 * x)) * (4 - x)) - (e ** (-0.5 * x))

    return ans

def newton_raphson(x0, es, iter_max) :
    iter_count = 0
    iter_count_list = []
    x_root = x0
    print("x0 =", x0)
    print()

    while True :
        last_x_root = x_root

        try :
            x_root = last_x_root - (f(x_root) / f_prime(x_root))
        except :
            print("total use", iter_count, "times.")
            return "Divergence"

        iter_count += 1
        iter_count_list.append(iter_count)
        if x_root != 0 :
            ea = abs((x_root - last_x_root) / x_root) * 100        

        print("iter time:", iter_count, ",ea =", ea, "root:", x_root)

        if (ea < es or iter_count >= iter_max) :
            print("total use", iter_count, "times.")
            return x_root

# %% [markdown]
# ### a. $x_0 = 2$

# %%
x0 = 2
es = 0.01
iter_max = 500

print("\nThe approximate ans:", newton_raphson(x0, es, iter_max))

# %% [markdown]
# ### b. $x_0 = 6$

# %%
x0 = 6
es = 0.01
iter_max = 500

print("\nThe approximate ans:", newton_raphson(x0, es, iter_max))

# %% [markdown]
# ### c. $x_0 = 8$

# %%
x0 = 8
es = 0.01
iter_max = 500

print("\nThe approximate ans:", newton_raphson(x0, es, iter_max))

# %% [markdown]
# 


