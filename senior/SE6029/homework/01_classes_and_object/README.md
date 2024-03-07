# Material 01 - Classes and Object

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
