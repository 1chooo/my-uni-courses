# Divide-and-Conquer

```cpp
Algorithm: Merge(A, p, q, r)
Input:
Output: 

nL = q - p + 1  // length of A[p:q]
nR = r - q      // length of A[q + 1:r]
let L[0: nL - 1] and R[0: nR - 1]

for i = 0 to nL - 1     // copy A[p:q] to temp L[]
    L[i] = A[p + i]

for j = 0 to nR - 1     // copy A[q + 1:r] tp temp R[]
    R[j] = A[q + j + i]

i = 0
j = 0
k = p

while i < nL and j < nR
    if L[i] <= R[j]
        A[k] = L[i]
        i = i + 1
    else
        A[k] = R[j]
        j = j + 1
    k = k + 1

while i < nL
    A[k] = L[i]
    i = i + 1
    k = k + 1

while j < nR
    A[k] = R[j]
    j = j + 1
    k = k + 1
```


```cpp
Algorithm: MergeSort(A, p, r)
Input: 
Output: 

if p >= r
    return 

q = floor((p + r) / 2)
MergeSort(A, p, q)
MergeSort(A, q + 1, r)

Merge(A, p, q, r)
```

* Divide: made sub-array into two adjacent sub-arrays, size is each of half the size.
* Conquer: sorting each of two sub-arrays and recursively using merge sort.
* Combine: merge two sorted sub-arrays to produce sorted answer.