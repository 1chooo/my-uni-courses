# %% [markdown]
# # [2022 Fall] Assignment4-4
# 
# > Course: AP3021

# %% [markdown]
# ## 4-4-a
# 
# ### Fixed-point iteration 
# to determine a root of $f(x) = -0.9x^2 + 1.7x + 2.5$ using $x_0 = 5.0$. Perform the computation until 𝜀𝑎 is less than 𝜀𝑠 = 0.01%. Also perform an error check of your final answer(plot the 𝜀𝑎 as the iteration growing)
# 
# ![plot](./src/imgs/A4_4_a.jpg)

# %%
import math
import matplotlib.pyplot as plt

# %%
def g(x) :
    ans = math.sqrt((1.7 * x + 2.5) / 0.9)

    return ans

# %%
def fix_point(x0, es, iter_max, ea_list, iter_count_list) :
    x_root = x0
    iter_count = 0

    while True :
        last_x_root = x_root
        x_root = g(last_x_root)
        iter_count += 1
        iter_count_list.append(iter_count)

        if (x_root != 0) :
            ea = abs((x_root - last_x_root) / x_root) * 100
            ea_list.append(ea)

        print("iter time:", iter_count, ",ea =", ea)
        if (ea < es or iter_count >= iter_max) :
            return x_root

# %%
x0 = 5
es = 0.01
iter_max = 500
ea_list = []
iter_count_list = []

print("\nThe approximate ans:", fix_point(x0, es, iter_max, ea_list, iter_count_list))
# print(ea_list)
# print(iter_count)

# %%
# plot

x = iter_count_list
y = ea_list

plt.plot(x, y)

plt.xlim(0, 10)
plt.ylim(0, 50)

plt.title("Growing of ea by fixed point iteration")
plt.grid()
plt.legend(["ea"], loc ="upper right")

plt.savefig("./src/imgs/A4_4_a.png", dpi=300)

plt.show()

# %% [markdown]
# ## 4-4-b
# 
# ### the Newton-Raphson method 
# to determine a root of $f(x) = -0.9x^2 + 1.7x + 2.5$ using $x_0 = 5.0$. Perform the computation until 𝜀𝑎 is less than 𝜀𝑠 = 0.01%. Also perform an error check of your final answer(plot the 𝜀𝑎 as the iteration growing)
# 
# ![plot](./src/imgs/A4_4_b.jpg)

# %%
def f(x) :
    ans = -0.9 * x ** 2 + 1.7 * x + 2.5

    return ans

# %%
def f_prime(x) :
    ans = -1.8 * x + 1.7

    return ans

# %%
def newton_raphson(x0, es, iter_max, ea_list, iter_count_list) :
    iter_count = 0

    while True :
        next_x = x0 - (f(x0) / f_prime(x0))
        x_root = next_x

        iter_count += 1
        iter_count_list.append(iter_count)

        ea = abs((x_root - x0) / x_root) * 100
        x0 = x_root
        ea_list.append(ea)
        

        print("iter time:", iter_count, ",ea =", ea)

        if (ea < es or iter_count >= iter_max) :
            return x_root

# %%
x0 = 5
es = 0.01
iter_max = 500
ea_list = []
iter_count_list = []

print("\nThe approximate ans:", newton_raphson(x0, es, iter_max, ea_list, iter_count_list))

# %%
# plot

x = iter_count_list
y = ea_list

plt.plot(x, y)

plt.xlim(0, 5)
plt.ylim(0, 50)

plt.title("Growing of ea by Newton Raphson")
plt.grid()
plt.legend(["ea"], loc ="upper right")

plt.savefig("./src/imgs/A4_4_b.png", dpi=300)

plt.show()


