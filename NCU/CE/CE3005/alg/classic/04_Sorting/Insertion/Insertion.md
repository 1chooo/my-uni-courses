Such as sorting a hand of playing cards,
then put the card into the right position.


```cpp
Algorithm: insertion sort
Input: A sequence of n numbers
Output: A permutation sequence

InsertionSort(A, n)
for i = 2 to n
    key = A[i]
    // Insert A[i] into the sorted subarray A[1: i - 1]
    j = i - 1
    while j > 0 and A[j] > key
        A[j + 1] = A[j]
        j = j - 1
    A[j + 1] = key
```


* Initialization: Before conducting, true.
* Maintenance: Remaining true before next iteration.
* Termination: When it terminates, shows that this algorithm is true.
* Analyzing:
  * input size
  * running time (quadratic function of n)
    * worst case
    * average case
    * rate of growth
    * order of growth
  * RAM
  


