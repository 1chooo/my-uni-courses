# Homework 2

## Homework 2-1
### Question: Evaluate the quantity $\sqrt{(c^2 + d)} -c$ to 4 correct significant figures, where c = 246886422468 and d = 13579.
### Answer: 

> 

###

## Homework 2-2
### Question: Find out the Python functions used to convert a floating point number into an integer.
### Answer: 

> The function to convert float type into integer type: `int()`
> 
> we can test two number: 
> 1. 10.0000000001
> 2. 10.9999999999
> 
> After using `int()` function, both turn into **10**.
> Therefore, we get the conclusion that when we use the function to convert the float type into integer type, the value after point will be ignored.

###

## Homework 2-3
### Question: What is the difference between the intrinsic `INT` and `NINT` functions in Fortran? Find the corresponding functions in Python.
### Answer: 

> The difference between two function in fortran.
> * `INT`: convert to integer. In python: int()
> * `NINT`: Round to nearest integer. In python: round()

###

## Homework 2-4
### Question: Convert the following base-2 numbers to base-10 
* 1011001 
* 110.00101
* 0.01011
### Answer: 

> | base-2    | base-10     |
> |-----------| ------------|
> | 1011001   | 89          |
> | 110.00101 | 6.15625     |
> | 0.01011   | 0.34375     |

###

## Homework 2-5
### Question: Compose your own program based on Fig. 3.11 and use it to determine your computer’s machine epsilon.
### Answer: 


### 

## Homework 2-6
### Question: 
### Answer: 

``` c
epsilon = 1

while (epsilon + 1 <= 1)
    epsilon /= 2

epsilon *= 2
```

###

## Homework 2-7
### Question: $x = \dfrac{x + \frac{a}{x}}{2}$, then find the root of a.
### Answer: 

``` py
def machineEpsilon() :
    epsilon = 1.0

    while (epsilon > 0) :
        xmin = epsilon
        epsilon = epsilon / 2

    return xmin
```

``` py
def IterMeth(val, es, maxIterator) :
    iter = 1
    sol = val
    ea = 100
    count = 1

    while True :
        solold = sol
        sol = (sol + (val / sol)) / 2
        iter = iter + 1

        if sol != 0 :
            ea = abs((sol - solold) / sol) * 100      

        if (ea < es or iter >= maxIterator) :
            break

        print(f"Times: {count}, Root: {sol :.4f}; Approximate relative error: {ea :.4f}%.")

        count += 1

    print("\nThe evaluate root:", sol)

    return sol
```

``` py
Machine eplison: 5e-324
What the value of "a" we picked up -> 25

Start evaluate: 
Times: 1, Root: 13.0000; Approximate relative error: 92.3077%.
Times: 2, Root: 7.4615; Approximate relative error: 74.2268%.
Times: 3, Root: 5.4060; Approximate relative error: 38.0226%.
Times: 4, Root: 5.0152; Approximate relative error: 7.7918%.
Times: 5, Root: 5.0000; Approximate relative error: 0.3045%.
Times: 6, Root: 5.0000; Approximate relative error: 0.0005%.
Times: 7, Root: 5.0000; Approximate relative error: 0.0000%.

The evaluate root: 5.0
```