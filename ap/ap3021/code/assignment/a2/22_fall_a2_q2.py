# %% [markdown]
# # [2022 Fall] Assignment2-2
# 
# > Course: AP3021
# 
# ### Question: Find out the Python functions used to convert a floating point number into an integer.
# ### Answer: 
# > The function to convert float type into integer type: `int()`
# > 
# > we can test two number: 
# > 1. 10.0000000001
# > 2. 10.9999999999
# > 
# > After using `int()` function, both turn into **10**.
# > Therefore, we get the conclusion that when we use the function to convert the float type into integer type, the value after point will be ignored.

# %%
# The function to convert float type into integer type.

print("The function we convert float type into integer type in python is: int()\n")

""" The example of the python code to convert float type to int type. """

print("====== The First Experiment ======")
# First we announce the float type number.
numberOne = 10.0000000001

print(f"The numberOne: {numberOne};\tType: {type(numberOne).__name__}.")

# After using the function, it will ignore the value after point.
numberOne = int(numberOne)
print(f"The converted numberOne: {numberOne};\tConverted type: {type(numberOne).__name__}.")

print("\n====== The Second Experiment ======")

# The next we can do another experiment, we announce the second number.
numberTwo = 10.9999999999
print(f"The numberTwo: {numberTwo};\tType: {type(numberTwo).__name__}.")

# After using the function, it still ignore the value after point.
# No matter the value after the point. The result is the same.
numberTwo = int(numberTwo)
print(f"The converted numberTwo: {numberTwo};\tConverted type: {type(numberTwo).__name__}.\n")

print("====== The conclusion ======")
print("Above all, we know that if we use function int() in python, no matter how value after the point, it will be losed.")


# %% [markdown]
# ![A2-2](./imgs/Picture2.jpg)

# %% [markdown]
# 


