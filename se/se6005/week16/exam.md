縱軸 困難度跟所耗費的時間

橫軸 解析度（程式的規模）

code coverage 有幾個部分


```java
public static void ascendingBubbleSort(int[] inputarray) {
    Boolean change;
    int temp;
    change = false;
    do {
        change = false;
        for (int i = 0; i < inputarray.length - 1; i++) {
            if (inputarray[i] > inputarray[i + 1]) {
                temp = inputarray[i];
                inputarray[i] = inputarray[i + 1];
                inputarray[i + 1] = temp;
                change = true;
            }
        }
    } while (change);
    // return inputarray; (if needed)
}
```
