# %% [markdown]
# # [2022 Fall] Assignment2-3
# 
# > Course: AP3021
# 
# ### Question: What is the difference between the intrinsic `INT` and `NINT` functions in Fortran? Find the corresponding functions in Python.
# ### Answer: 
# 
# > The difference between two function in fortran.
# > * `INT`: convert to integer. In python: int()
# > * `NINT`: Round to nearest integer. In python: round()

# %% [markdown]
# ```f90
# program test_int
#     implicit none
#     
#     integer :: i = 42
#     complex :: z = (-3.7, 1.0)
#     print *, int(i)
#     print *, int(z), int(z,8)
# 
#     stop
#   end program
# ```

# %% [markdown]
# ![A2-3](./imgs/Picture3.jpg)

# %% [markdown]
# 


