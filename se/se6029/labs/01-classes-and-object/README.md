# Material 01 Lab - Classes and Object   <!-- omit from toc -->

**Table of Contents**
- [Course](#course)
  - [Lab 02](#lab-02)
  - [Lab 03](#lab-03)
  - [Lab 04](#lab-04)
  - [Lab 05](#lab-05)
  - [Lab 06](#lab-06)
  - [Lab 08](#lab-08)
  - [Lab 10](#lab-10)
  - [Lab 13](#lab-13)
- [Take Home](#take-home)
  - [Homework - Lab 01](#homework---lab-01)
  - [Homework - Lab 07](#homework---lab-07)
  - [Homework - Lab 12](#homework---lab-12)
  - [Homework - Lab 14](#homework---lab-14)

## Course

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

### Lab 04

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


--- 

## Take Home

### Homework - Lab 01

Please write a correct programmer/manager class in C++

**PPT Source Code:**
```cpp
#include <iostream>
using namespace std;
class Employee
{
public:
    Employee(char *name, int id);
    ~Employee();
    char *getName() { return _name; }
    // Other Accessor methods
private:
    int _id;
    char *_name;
};
Employee::Employee(char *name, int id)
{
    _id = id;
    _name = new char[strlen(name) + 1];
    // Allocates an character array object
    strcpy(_name, name);
}

Employee::~Employee()
{
    delete[] _name;
}
int main()
{
    Employee programmer("John", 22);
    cout << programmer.getName() << endl;
    return 0;
}
```

**Ans:**

```cpp
class Employee {
  public:
    Employee(char *name, int id);
    Employee(Employee &rhs);
    ~Employee();
    char *getName() { return _name; }
    int getId() { return _id; }
    // Other Accessor methods
  private:
    int _id;
    char *_name;
};
```


### Homework - Lab 07

假設有以下兩個 class，請幫我們實作 Foo 類別的解構子，複製建構子和賦值運算子 

> [!TIP]
> (相信我，這題不像看起來的那麼簡單，請考慮 exception-safe 和 memory leak 的各種可能問題) (參考：http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-ctor)


```cpp
#include <array>

class Bar {
private:
    std::array<int, 30> not_important_;
};

class Foo {
public:
    Foo()
        : bar_{new Bar{}} {}

    // Rule of three!
    Foo(const Foo& rhs) {
        // TODO: Not yet implemented.
        std::terminate();
    }

    Foo&
    operator=(const Foo& rhs) {
        // TODO: Not yet implemented.
        std::terminate();
    }

    ~Foo() {
        // TODO: Not yet implemented.
        std::terminate();
    }

private:
    // XXX: Well, this is not doing well in practical...
    // but hey, this is just some exercise. Please use
    // std::unique_ptr or std::shared_ptr instead.
    //
    // The Foo object will "own" this Bar pointer.
    Bar* bar_{nullptr};
};
```

**Ans:**

```cpp
Foo(const Foo &rhs) {
    // TODO: Not yet implemented.
    bar_ = new Bar{*rhs.bar_};
}

Foo &operator=(const Foo &rhs) {
    // TODO: Not yet implemented.
    if (this != &rhs) {
        delete bar_;
        bar_ = new Bar{*rhs.bar_};
    }
    return *this;
}

~Foo() {
    // TODO: Not yet implemented.
    delete bar_;
}
```

### Homework - Lab 12

There is a compile error with the C++ code. Please point out the line number and explain why

```cpp
class A {
    public:
    A();
};
A arrayA[10];

class B {
    public:
    B();
};
B arrayB[10];

class C {
    C(int x);
};
C arrayC[10];
```

**Ans:**

The compile error occurs in line 12: `C(int x);` and line 14: `C arrayC[10];`.

The reason for this error is that the class C has a constructor that takes an integer argument, but no **default constructor**. When declaring an array of `C` objects like `C arrayC[10];`, the compiler needs to be able to call a default constructor to initialize each of the objects in the array. Since class `C` does not have a default constructor, this results in a compile error.

To fix this compile error, we cab provide a default constructor for class `C`:

```cpp
class C {
public:
    C() {} // Default constructor without any parameters
    C(int x);
};
```

Or we could initialize the array at the time of declaration:

```cpp
C arrayC[10] = {C(0), C(0), C(0), C(0), C(0), C(0), C(0), C(0), C(0), C(0)};
```

### Homework - Lab 14

當你在撰寫 assign operator 時，其格式上大致如下 (以 String 型別為例)

```cpp
String& String::operator=(const String& rhs) {
    ...
    return *this ;
}
```

請問說明為何這個 method 要回傳自己?

**Ans:** [^1]

`asign` 的設計就是由右向左，基本數據類型支持賦值運算符的鏈式操作：

```cpp
int a, b, c;
a = b = c = 5;
```

因此自定義類型也應該支持賦值運算符的鏈式操作：

```cpp
string w, x, y, z;

w = x = y = z = "Hello"; // Assigning "Hello" to z, then y, then x, then w.
w = (x = (y = (z = "Hello")));  // The previous line can be parsed as
w.operator=(x.operator= (y.operator=(z.operator=("Hello"))));  // Equivalent functional form
```

> [!NOTE]
> 要支持鏈式操作，返回值必須是對象的引用才行。

標準 String 類型提供了兩個不同版本的賦值運算符：

```cpp
string& operator=(const string& rhs); string& operator=(const char *rhs);
```

採用預設形式定義的賦值運算符里，對象返回值有兩個很明顯的候選者：看看下面哪一個是正確的？以String 類為例：

```cpp
String& String::operator=(const String& rhs) { 
    ... 
    return *this; // return the left-hand object
} 

String& String::operator=(const String& rhs) { 
    ... 
    return rhs; // return the right-hand object
}
```

return the right-hand object one won't be compiled, because `rhs` is the reference of `const String` object, and `*this` is the reference of the `& String`.

Therefore, this method will `return *this;`

[^1]: [Effective C++ 讀書筆記15: 讓 operator=返回*this 的引用](https://kknews.cc/code/a2gyp8x.html)
