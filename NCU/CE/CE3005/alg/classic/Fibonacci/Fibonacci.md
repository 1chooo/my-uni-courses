# Fibonacci


### Pseudocode

<br>

```cpp
Algorithm: Fibonacci(n)
Input: integer n
Output: The nth factor in Fibonacci array.

if (n = 1 or n = 2) then
    return 1
else
    a <- 1
    b <- 1

    for i = 3 to n do
        c <- a + b
        a <- b
        b <- c
    
    return c
```

<br>

```cpp
Algorithm: RecursiveFibonacci(n)
Input: integer n
Output: The nth factor in Fibonacci array.

if (n = 1 or n = 2) then
    return 1
else
    a <- RecursiveFibonacci(n - 1)
    b <- RecursiveFibonacci(n - 2)

    return (a + b)
```
