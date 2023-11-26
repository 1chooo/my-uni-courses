# %% [markdown]
# # [2022 Fall] Assignment4-6
# 
# > Course: AP3021

# %% [markdown]
# ## 4-6-1
# 
# If R = 3 m, what depth must the tank be filled to so that it holds 30 𝑚3?
# 
# ![plot](./src//imgs/A4_6_1.jpg)
# 

# %% [markdown]
# ## 4-6-2
# 
# Newton-Raphson method (3 iterations; determine relative error after each iterations)(Python)
# 

# %%
import math

# %%
def f(h, R, V) :
    PI = math.pi
    ans = PI * (h ** 2) * (((3 * R) - h) / 3) - V

    return ans

# %%
def f_prime(h, R) :
    PI = math.pi
    ans = (2 * PI * h * R) - (PI * (h ** 2))

    return ans

# %%
def newton_raphson(x0, es, iter_max, R, V) :
    iter_count = 0
    iter_count_list = []
    x_root = x0
    print("x0 =", x0)
    print()

    while True :
        last_x_root = x_root

        try :
            x_root = last_x_root - (f(x_root, R, V) / f_prime(x_root, R))
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

# %%
R = 3
V = 30
x0 = R
es = 0.01
iter_max = 3

print("\nThe constrains of h:", newton_raphson(x0, es, iter_max, R, V))

# %% [markdown]
# ## 4-6-3
# 
# What are the constraints of h?

# %%
print("\nThe constrains of h:", newton_raphson(x0, es, iter_max, R, V))

# %%



