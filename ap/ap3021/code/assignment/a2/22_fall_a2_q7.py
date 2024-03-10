# %% [markdown]
# # [2022 Fall] Assignment2-7
# 
# > Course: AP3021
# 
# ### Question: $x = \dfrac{x + \frac{a}{x}}{2}$, then find the root of a.
# ### Answer: 

# %%
# First through the machine eplison. (HW2-5)

def machineEpsilon() :
    epsilon = 1.0

    while (epsilon > 0) :
        xmin = epsilon
        epsilon = epsilon / 2

    return xmin


def IterMeth(val, es, maxIterator) :
    iter = 1
    sol = val
    ea = 100
    count = 1

    while True :
        preSol = sol
        sol = (sol + (val / sol)) / 2
        iter = iter + 1

        if sol != 0 :
            ea = abs((sol - preSol) / sol) * 100      

        if (ea < es or iter >= maxIterator) :
            break

        print(f"Times: {count}, Root: {sol :.4f}; Approximate relative error: {ea :.4f}%.")

        count += 1

    print("\nThe evaluate root:", sol)

    return sol

print("Machine eplison:", machineEpsilon())
print("What the value of \"a\" we picked up -> 25\n")
print("Start evaluate: ")

IterMeth(25, machineEpsilon(), 100)

# %% [markdown]
# ### C Language Version

# %% [markdown]
# ```c
# #include <stdio.h>
# #include <math.h>
# 
# double preAbs(double), machineEpsilon(void), IterMeth(double, double, double);
# 
# double preAbs(double x) {
#   if (x < 0)
#     x = -x;
# 
#   return x;
# }
# 
# double machineEpsilon(void) {
#   double epsilon = 1.0, xmin;
# 
#   while (epsilon > 0) {
#     xmin = epsilon;
#     epsilon = epsilon / 2;
#   }
# 
#   return xmin;
# }
# 
# double IterMeth(double val, double es, double maxit) {
#   double iter = 0.0, sol = val, ea = 100.0, solold;
# 
#   while (1) {
#     solold = sol;
#     sol = (sol + val / sol) / 2;
#     iter += 1.0;
# 
#     if (sol != 0)
#       ea = preAbs((sol - solold) / sol) * 100;
# 
#     printf("%g %g\n", sol, ea);
# 
#     if ((ea <= es) || (iter >= maxit))
#       break;
#   }
# 
#   return sol;
# }
# 
# int main() {
#   double a;
# 
#   printf("Input a: ");
#   scanf("%lf", &a);
#   printf("%g", IterMeth(a, machineEpsilon(), 100));
#   printf("\n");
# 
#   return 0;
# }
# ```

# %% [markdown]
# 


