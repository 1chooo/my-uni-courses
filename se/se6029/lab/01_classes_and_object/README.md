# Material 01 - Classes and Object

### Lab 02
Please answer what’s wrong with the following code
```cpp
Car * foo() {
    Car  mazda ;
    ...
    return &mazda ;
}
```

- My Ans: dangling pointer, Car mazda 要用 new 的方式！
- Prof Ans: 怕 mazda 是 local variable 怕把 stack return 到上一層，return 會清除掉，如果內容物讓上層去存取，可能 run 一 run 會當掉，因為 mazda 已經被清掉了。


### Lab 03
```cpp
#include <iostream>
using namespace std ;
class Table {
    char *p ;
    int sz ;
public:
    Table(int s=15) { 
        p = new char[100] ;
        cout << "constructor" << endl ;
         } 
    ~Table() { delete[] p ; 
      cout << "destructor" << endl ; 
      }
};
void h() {
    Table t1 ;      // Default constructor is called
    Table t2 = t1 ; // No Default constructor is called，compiler default is called
    Table t3 ;      // Default constructor is called
    t3 = t2 ;       // No constructor, deconstructor is called
}
main() { h(); }     // Destructor is called three times
```


- How many times the default constructor is called? 
- How many times the default destructor is called?
- What is the final output? And why?


My Ans:
1. 2 times 
2. 1 time 
3. malloc: Double free of object

## Lab 04

請用你的語言，向我們解釋object和class的不同之處。不限制語言，能表達你的論點即可。

My Ans:
- What is a class ? (一個 type)
  - class is just a type
  - When you define a class X，you pass another X.h to be included by others.
  - Without X.obj, it is still possible for others to compile his module.
  - In C++, a class is just like a primitive type INT, CHAR

- What is an object? (有記憶體的變數)
  - When you use a class to create a variable, the variable (along with its allocated memory) is called an object
  - A class can have many objects
  - Each object has its own memory
  - Object is simply memory+behaviors (code)


### Lab 05

在設計class時，你覺得什麼情況需要由程式設計師提供解構子(destructor)？

My Ans:

如個 class 裡面有用到 stack 跟 heap 的 segment 的時候，需要去主動去釋出，以避免佔用過多的記憶體導致 stack overflow, out of memory

Prof Ans:

```cpp
class OO {
    int a[1000];    // 4000 byte
    int b;          // 4 byte
    char abc;       // 1 byte
    char *p;        // 這裡就額外配置動態記憶體
}
```

### Lab 06

請問，一個 class 的 destructor 何時會被呼叫？

- My Ans:

    function 結束的時候需要被 clear 掉的時後

- Prof Ans:

    如果物件是 local variable，如果程式需要主動 delete，用 class 來宣告 global variable，程式結束的時候會被呼叫


### Lab 08

什麼時候 copy constructor 會被呼叫？ 請用一句話來說明。

- (WRONG) My Ans:

  `copy` operator 會初始化一塊未經初始化的記憶體

- Prof Ans:

```cpp
OO y = x;
OO y;
```


### Lab 10

copy constructor 與 assign operator 有什麼不同？

- My Ans: 
    `copy` constructor 會初始化一塊未經初始化的記憶體 (牽涉到一個新的變數或物件的建立)，而 `=` operator 必須妥善處理一個已經建構好的的物件 (`=` 沒有)


### Lab 13

In C++, you can still use pass-by-value to pass an object to a function, such as:


```cpp
void foo(X a) {
    …….
}

main() {
    X b ;
    foo(b);
}
```

Please explain
1. how C++ compiler implement the pass-by-value for you.
2. why it is not recommended to use pass-by-value to pass an object?

- My Ans:
1. b 的 address 會給到 a 
2. 因為在 C++ 中會建立兩個 a, b 的兩個記憶體段，因此不建議直接這樣共用

- Prof Ans:
`object size = 100 bytes`

`Python/JAVA`
```
int x;      // 4 byte
object x;   // 宣告時只會有一個指標，不會配置記憶體空間
```

`C++`
```cpp
int x;      // 4 byte
object x;   // 會直接配置記憶體空間
```

在 `C++` 叫做 **Pass by Value**，在 `Python` 叫做 **Pass by Reference**

呼叫 `foo()` 會 copy 一份 constructor 會複製一段到 `Stack`