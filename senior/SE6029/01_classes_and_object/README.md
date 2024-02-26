# Material01 - Classes and Object

### What is a class ?

- class is just a type
- When you define a class X，you pass another X.h to be included by others.
- Without X.obj, it is still possible for others to compile his module.
- In C++, a class is just like a primitive type INT, CHAR

### What is an object?

- When you use a class to create a variable, the variable (along with its allocated memory) is called an object
- A class can have many objects
- Each object has its own memory
- Object is simply memory+behaviors (code)

```cpp
class Point {
          int z ;
    public:
          int x ;
          int y ;
};

Point  p,p1 ;
main() {
     p.x = 100;
     p.y = 200 ;
}
```

規格與定義是分開的

- 規格 class
- 定義 code (behavior)

### 執行檔案載入記憶體中的位置

`sbrk()`: use to find the initial address of the heap [^1]

```
+----------------------+
|       Data           |  <- Global Variable
+----------------------+
|      SysCode         |
+----------------------+
| Heap (top to bottom) |  <- If too much is allocated, it encounters Stack -> Out of Memory (Memory Leak)
|         ...          |
|                      |
|                      |
|         ...          |
| Stack (bottom to top)|  <- If too much is allocated, it encounters Heap -> Stack Overflow
+----------------------+
|       Kernel         |
+----------------------+
```

#### What's Heap?

- Heap in a process’s image (let’s rock)
- In `C`
  - use `malloc`, `calloc`, `free`
- In `C++`,
  - use `new`, `delete`
  - Be aware of **memory leaking**

Just like C, you have 3 places to place your object

- data (life time goes with program)
- stack (life time goes with functions)
- heap (life time vary)

### Exercise

What's wrong with the following code?

```cpp
Car* foo() {
    Car  mazda ;
        :
        :
    return &mazda ;
}
```

這個程式中有一個潛在的問題是，函數`foo()`嘗試返回一個指向本地變量`mazda`的指針。當函數返回時，本地變量`mazda`將被銷毀，這將導致返回的指針指向一個已經無效的內存位置。這可能導致未定義的行為，例如訪問無效的內存或崩潰。

要解決這個問題，可以通過動態分配內存來創建一個`Car`對象，並在返回指針之前確保不要在函數結束時銷毀該對象。例如，可以使用`new`運算符來動態分配內存，然後在不再需要時使用`delete`來釋放內存。下面是修正的示例：

```cpp
Car* foo() {
    Car* mazda = new Car();
    // 對 mazda 做一些操作
    return mazda;
}
```

在這個修正版本中，返回的是一個指向堆上動態分配的`Car`對象的指針，而不是指向本地變量。這樣可以確保在函數返回後該對象仍然存在，並且指針仍然有效。當不再需要時，應該通過`delete`來釋放內存，以避免內存泄漏。

---

## Dynamic Memory Allocation

這十個 `tbl` 一定有一個 `Table` 是沒有參數的建構子 `Table :: Table()`，否則會有 Compiler Error。
```cpp
Table tbl[10];  // constructor Table() will be called 10 times

delete[] tbl ;
```

```cpp
int *IDpt = new int;            // (in C) int *IDpt = malloc(sizeof(int));
float *theMoney = new float; 
char *letter = new char; 
```

The "new" operator returns the address to the start of the allocated block of memory. This address must be stored in a pointer. New allocates a block of space of the appropriate size in the heap for the object. Dynamically allocated memory is accessed indirectly via a pointer. It is possible for new to fail. This will be the case if no memory is available. In this case new throw a `bad_alloc` exception. Exception handling will be discussed in a latter lesson. 


```cpp
int *IDpt = new int; 
*IDpt = 5;  
int *IDpt = new int(5);         // Allocates an int object and initializes it to value 5. 
char *letter = new char('J'); 
```

```cpp
delete IDpt; 
delete theMoney; 
delete letter; 
```


### Dynamic allocated array

```cpp
int *pt = new int[1024];    //allocates an array of 1024 ints
double *myBills = new double[10000];

int *pt = new int[1024];    //allocates an array of 1024 ints
int *pt = new int(1024);    //allocates a single int with value 1024 
```

A dynamically allocated array is best initialized using a loop, as follows. 

```cpp
int *buff = new int[1024]; 
for (i = 0; i < 1024; i++) { 
    buff[i] = 52; 	// Assigns 52 to each element; 
    buff++; 
}
```

free the dynamic allocated objects

```cpp
delete[] pt; 
delete[] myBills;   // chapter11() will also release the memory :-)  
```




[^1]: [系统调用与内存管理 (`sbrk、brk、mmap、munmap`)](https://blog.csdn.net/Apollon_krj/article/details/54565768)
