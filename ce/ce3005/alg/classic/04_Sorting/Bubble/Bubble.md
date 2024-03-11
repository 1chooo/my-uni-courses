# Bubble Sort

是個簡單的排序演算法，透過一次比較兩兩元素進而達成排序，
stable
不需要額外記憶體，就地演算法

<br>

### Pseudocode

<br>

``` cpp
Algorithm: BubbleSort(A, n)
Input: Array A with nth integer.
Output: Array A which ordered from least to greatest.

for i = (n - 1) to 1 do
    for j = 0 to (i - 1) do
        if A[j] > A[j + 1] then
            swap(A[j], A[j + 1])

return A
```