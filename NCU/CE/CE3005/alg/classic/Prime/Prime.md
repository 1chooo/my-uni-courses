# Prime Check

### Pseudocode

<br>

```cpp
Algorithm: PrimeCheck(n)
Input: A integer n greater than 2
Output: true or false

for i = 2 to n - 1 do
    if (n % i) = 0 then
        return false

return true
```

<br>

```cpp
Algorithm: PrimeCheck2(n)
Input: A integer n greater than 2
Output: true or false

for i = 2 to sqrt(n) do
    if (n % i) = 0 then
        return false

return true
```