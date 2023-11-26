# %% [markdown]
# # [2022 Fall] Assignment4-3
# 
# > Course: AP3021

# %% [markdown]
# ## 4-3-1
# 
# Develop a user-friendly subprogram for the modified false-position method based on Fig. 5.15. Test the program by determining the root of the function described in Example 5.6. Perform a number of runs until the true percent relative error falls below 0.01%. (Python)

# %%
def f(x) :
    ans = x ** 10 - 1

    return ans

# %%
def count_ea(new_x_root, old_x_root) :

    if (old_x_root == -1) : # jump out the first data.
        return 9999
    else :
        ea = abs((new_x_root - old_x_root) / new_x_root)
        ea = ea * 100   # turn into percent
    
    return ea

# %%
def count_et(true_value, approximation) :
    true_error = true_value - approximation
    et = abs((true_error / true_value) * 100)

    return et

# %%
def ModFalsePos(x_lowwer, x_upper, x_root, es, iter_max, iter_count_list, ea_list, et_list) :
    iter_count = 0
    iter_upper, iter_lowwer = 0, 0
    lowwer_value = f(x_lowwer)
    upper_value = f(x_upper)

    while True :
        last_x_root = x_root
        x_root = x_upper - upper_value * (x_lowwer - x_upper) / (lowwer_value - upper_value)
        root_value = f(x_root)

        iter_count += 1
        iter_count_list.append(iter_count)

        if (x_root != 0) :
            ea = count_ea(x_root, last_x_root)
            ea_list.append(ea)

        true_value = 1

        et = count_et(true_value, x_root)
        et_list.append(et)

        temp = lowwer_value * root_value

        if (temp < 0) :
            x_upper = x_root
            upper_value = f(x_upper)
            iter_upper = 0
            iter_lowwer += 1

            if (iter_lowwer >= 2) :
                lowwer_value /= 2
        elif (temp > 0) :
            x_lowwer = x_root
            lowwer_value = f(x_lowwer)
            iter_lowwer = 0
            iter_upper += 1

            if (iter_upper >= 2) :
                upper_value /= 2
        else :
            ea = 0.0
        
        print("count", iter_count, "ea", ea, "root", x_root)
        
        if (ea < es or iter_count >= iter_max) :
            return x_root

# %%
x_lowwer = 0
x_upper = 1.3
x_root = -1
true_percent_relative_error = 0.01 # 0.01%
iter_max = 500
iter_count_list = []
ea_list = []
et_list = []

x_root = ModFalsePos(x_lowwer, x_upper, x_root, true_percent_relative_error, iter_max, iter_count_list, ea_list, et_list)

print("\nthe approximate root:", x_root)

# %% [markdown]
# ## 4-3-2
# 
# Plot the true and approximate percent relative errors versus number of iterations. (Python)

# %%
import matplotlib.pyplot as plt

# %%
# plot ea and et

ea_list[0] = 99     #the first element is neglected.
x = iter_count_list
y1 = ea_list
y2 = et_list

plt.plot(x, y1)
plt.plot(x, y2)

plt.xlim(0.9, 13)
plt.ylim(0, 100)
plt.xlabel("iteration")
plt.ylabel("percent")

plt.title("et and ea versus number of the iterations")
plt.grid()
plt.legend(["ea", "et"], loc ="upper right")

plt.savefig("./src/imgs/A4_4_2.png", dpi=300)

plt.show()

# %%



