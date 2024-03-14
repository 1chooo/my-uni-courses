# Material 03 - PolyMorphism

## Course

### Lab 01

Some programmer wrote the following code:

```cpp
class base_model {
   ...
};

class model: base_model {
   ...
};

// Other places which use the classes above
   ...
   model m = new model();
   ...
```

He explains that he is doing great in inheritance and polymorphism.What do you think? (請你給他洗臉一下)

**My Ans:**

```cpp
model m = new model();
```

宣告一個 `model m` 並且還用 `new model()` 並不是個好的做法，也沒有達到多型的目的，可以針對特定目標做出不同操作

Polymorphism in C++ is exhibited by the ability of a pointer or reference to a base class type to behave in different ways when it is used to manipulate objects of different subtypes of that base class. 

多形就是當你可以用基底 class 的指標或參考來進行處理時，卻可以依照其 subtype 來進行不一樣的事情（其實多形是很難用解釋的）


### Lab 02

Why destructor in C++ must be declared as virtual?

**My Ans:**

因為當我們繼承原本的 base class 的時候我們是用原本的記憶體繼續增加，因此當我們今天要 destructor 新繼承的 class 的時候，我們的 destructor 是要用掉新建立的記憶體



### Lab 05

Why not make an abstract class to have all the methods to be abstract and enforce its subclasses to implement each method? 

Such as:
```cpp
class Human {
      public:
         virtual void walk() = 0 ;
         virtual void breath() = 0 ;
         virtual void speak()=0;
};
```

Please describe the pros and cons if you choose to do so. (本題分數為其它題目的3倍)


### Lab 06

What is dynamic binding?

**My Ans:**

我們今天在 class 的記憶體中，會有個 pointer  幫我們指向虛擬的函式表，當我們今天要用的資源在 dynmic 的地方時可以幫我們指過去使用


### [NEED TO SEARCH] Lab 07

Please explain:

1. compilation time binding
2. linking binding
3. loading time binding

**My Ans:**
1. 在編譯的時候就確定要綁定哪一個 -> static
2. 編譯的時候知道要使用的函示 address，透過只過去使用的編譯的時候就會知道
3. 載入的時候，也就是開始運行時動態地去調用



### [NEED TO SEARCH] Lab 08

What is an indirect call in assembly? Please explain and give an example.


當我們今天要呼叫目標函數的時候，也就是 `CALL`

```assembly
GOAL_FUNCTION :
... adress

mov eax, GOAL_FUNCTION
call eax
```

我們會先載入目標函數，透過呼叫的方式去執行



### Lab 09

In C++ You can use `sizeof()` to print the memory size of an object.

```cpp
class base {
   public:
   int x ;
   int y ;
   virtual void dosomething() { } ;
};
```

Typically, an integer is 4 bytes. What is the size of an object from base?

Why?


16 bytes

int x, y 總共 8 bytes 

不過 dosomething 時我們用的是 virtual function 因此有個 8 個 bytes

要放 pointer 指到 virtual function table


### Lab 10

填充題:

物件導向最重要的核心意義就是將系統中 _____________ 的部分包裝到子類別中，然後利用 ______________將系統中的 high-level components (core components) 寫成與子類別 _______________的程式碼。所以當未來進行擴充或修改時， high-level components (core components) 可以幾乎都不用打開來修改。

1. 未來或者頻繁變異、擴充
2. 多型 Polymorphism
3. 無關 inrelevant, independent

--- 

## Homework



