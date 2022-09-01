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

* Best case: 1 = O(1)
* Worst case: n - 2 = O(n)

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

* Best case: 1 = O(1)
* Worst case: sqrt(n) - 1 = O(sqrt(n))