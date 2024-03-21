# Material 04 - Multiple Inheritance  <!-- omit from toc --> 

**Table of Contents**
- [Introduction](#introduction)
- [Percolating Up](#percolating-up)
- [A smarter solution?](#a-smarter-solution)
  - [In Java](#in-java)
- [Casting in C/C++](#casting-in-cc)
  - [Outputs](#outputs)
- [Analysis of the Ambiguity](#analysis-of-the-ambiguity)
  - [Solution 1: Casting Ambiguous Attributes or Methods](#solution-1-casting-ambiguous-attributes-or-methods)
  - [Solution 2: Overwriting Ambiguous Attributes or Methods](#solution-2-overwriting-ambiguous-attributes-or-methods)
  - [Another Case: JetCar](#another-case-jetcar)
  - [Another Case: Storable](#another-case-storable)
    - [Diamond-Shaped Inheritance](#diamond-shaped-inheritance)
  - [Java Interface](#java-interface)
    - [How to use Java interface?](#how-to-use-java-interface)
    - [Discussion of Java Multiple Inheritance](#discussion-of-java-multiple-inheritance)
    - [To simulate interface in C++](#to-simulate-interface-in-c)


> [!IMPORTANT]
> Polymorphism 與未來擴充的型別無關

## Introduction

```cpp
#include <iostream>

using namespace std;

class Vehicle {
  public:
    Vehicle() { cout << "Vehicle Constructor" << endl; }
    virtual ~Vehicle() { cout << "Vehicle Destructor" << endl; }
    virtual void accelerate() const { cout << "Vehicle Accelerating" << endl; }
    void setAcceleration(double a) { acceleration = a; }
    double getAcceleration() const { return acceleration; }

  private:
    double acceleration;
};

class Car : public Vehicle {
  public:
    Car() { cout << "Car Constructor" << endl; }
    virtual ~Car() { cout << "Car Destructor" << endl; }
    virtual void accelerate() const { cout << "Car Accelerating" << endl; }
    void drive() const { cout << "Car Driving" << endl; }

  private:
    // Car inherits acceleration accessors, member
};

int main() {
    Car myCar;
    myCar.setAcceleration(9.81); // One "G"
    cout << "Accelerating at " << myCar.getAcceleration() << " m/(s*s)";
    cout << endl;

    myCar.accelerate();
    myCar.drive();
}
```


> [!NOTE]
> - `accelerate()` is declared as `virtual` -> can be overridden. -> it is automatically `virtual` in all subclasses.
> - If using the keyword **`virtual`** in Car -> learer that `accelerate()` is a `virtual` method. -> Another programmer, looking only at the Car class, would know that the method was `virtual`.
> `setAcceleration()` and `getAcceleration()`, are non `virtual`. -> don't expect to override them in any subclasses, but rather just inherit them. Notice that the `Car` class has indeed inherited these methods.


```cpp
class JetCar : public Car {
    public:
        JetCar() {}
        virtual ~JetCar() {}
        virtual void drive() const { cout << "JetCar driving" << endl; }
        virtual void fly() const { cout << "JetCar flying" << endl; }
    };
}

/*
-----------------------
some function elsewhere
-----------------------
*/

void analyzePerformance(Car *testVehicle) {
    testVehicle->drive();
    testVehicle->fly();
}
```

- the `drive()` method of `JetCar` override the the `drive()` of car because the driving method of jetcar should be a little different from car
- because `JetCar` can fly, so a new method called `fly()` is added and is prepared to be overridden

> [!WARNING]
> There is an error in compilation in `analyzePerformance` 
> 
> -> car does not have a fly method only JetCar does

```bash
drive.cpp:44:18: error: no member named 'fly' in 'Car'
    testVehicle->fly();
    ~~~~~~~~~~~  ^
1 error generated.
```

## Percolating Up

```cpp
class Car : public Vehicle {
  public:
    Car() {}
    virtual ~Car() {}
    virtual void accelerate() const { cout << "Car Accelerating" << endl; }
    virtual void drive() const { cout << "Car Driving" << endl; }
    virtual void fly() const { cout << "Cars can only fall" << endl; }

  private:
    // Car inherits acceleration accessors, member
};

class JetCar : public Car {
  public:
    JetCar() {}
    virtual ~JetCar() {}
    virtual void drive() const { cout << "JetCar driving" << endl; }
    virtual void fly() const { cout << "JetCar flying" << endl; }
};

int main() {
    Car myCar;
    JetCar myJetCar;
    analyzePerformance(&myCar);
    analyzePerformance(&myJetCar);
    return 0;
}
```

We get the correct result.

- The Car class has a "fly" method. Surely, Cars don't fly. We added the fly method to Car so that a base class pointer could be used on either. This is known as **percolating upward**. 
- The fly method was moved up into a base class, but the base class Car should not have that functionality. 
- If we percolated up more methods as we built these classes, Car becomes **bloated and confused**. Generally, only functionality common to all subclasses belongs in a base class.

## A smarter solution?

```cpp
class Car : public Vehicle {
  public:
    Car() {}
    virtual ~Car() {}
    virtual void accelerate() const { cout << "Car Accelerating" << endl; }
    virtual void drive() const { cout << "Car Driving" << endl; }

  private:
    // Car inherits acceleration accessors, member
};
class JetCar : public Car {
  public:
    JetCar() {}
    virtual ~JetCar() {}
    virtual void drive() const { cout << "JetCar driving" << endl; }
    virtual void fly() const { cout << "JetCar flying" << endl; }
    // 如果我們要加上 SubmarineCar，我們無法做到萬年不動，除了要加一個新的 class 還要找到這裡修改，我們應該要做到「跟未來擴充的型別無關」
};

void analyzePerformance(Car *testVehicle) {
    JetCar *ptr;
    // A pointer of subclass type, JetCar
    testVehicle->drive();
    // drive() exists for both base and sub class
    ptr = dynamic_cast<JetCar *>(testVehicle);      // cast down to JetCar pointer
    if (ptr) {
        ptr->fly();
    } else {
        cout << "Car being tested" << endl;
    }
}

int main() {
    Car myCar;
    JetCar myJetCar;
    analyzePerformance(&myCar);
    analyzePerformance(&myJetCar);
    return 0;
}
```

- C++ has a built in mechanism for **Runtime Type Identification, RTTI**. This means that as a program is running it is possible to determine the exact type of object a pointer or reference refers to. 
- RTTI is achieved in C++ via the `dynamic_cast` operator, the `typeid` operator and the `type_info` class. 
- The `dynamic_cast` operator returns a pointer to type `JetCar` if have the address of a `JetCar` object in the original pointer, `testVehicle`. Otherwise, the `dynamic_cast` operator returns `NULL`. 
- Dynamic casting used in this manner is referred to as "casting down". We have casted a base class pointer down its hierarchy into a subclass pointer. 

> [!NOTE]
> Casting up: `Car *p = (Car *) new JetCar();`

### In Java

In Java you can use `instanceof`

For example:
```java
analyzePerformace (Car testvehicle) {
    if (testvehicle instanceof JetCar) {
        ...
    }
```

> [!WARNING]
> That is BAD!!!
>
> - Explicitly checking an objects type is usually indicative of bad design  
> - Generally, you should avoid explicitly testing the type of an object in your code. 
> - Why? As told in **spaghetti code course**. As additional classes are formed, every point in the code that makes explicit checks on object type may need modification. If you forget to modify code somewhere, you may not find out until your program fails and your JetCar careens off into the sun. For practice, consider what modifications would be needed to support my next project, the BoatCar.

## Casting in C/C++

```cpp
ptr = dynamic_cast <JetCar *>(testVehicle); // Dynamic Cast
ptr = static_cast <JetCar *>(testVehicle); // Static Cast 
ptr = (JetCar *) testVehicle; // C style static cast
```

> [!IMPORTANT]
> In Visual C++, RTTI is not turned on by default, if you run this code without turning on RTTI, you will get a **cryptic error message saying something like "'dynamic_cast' used on polymorphic type 'Car' with /GR-; unpredictable behavior may result".** Turning on RTTI allows the compiler to insert additional code to support RTTI as it forms object files. 


```cpp
#include <iostream>

using namespace std;

class Vehicle {
  public:
    Vehicle() { cout << "Vehicle Constructor" << endl; }
    virtual ~Vehicle() { cout << "Vehicle Destructor" << endl; }
    virtual void accelerate() const { cout << "Vehicle Accelerating" << endl; }
    void setAcceleration(double a) { acceleration = a; }
    double getAcceleration() const { return acceleration; }

  protected:
    double acceleration;
};

class Car : public Vehicle {
  public:
    Car() { cout << "Car Constructor" << endl; }
    virtual ~Car() { cout << "Car Destructor" << endl; }
    virtual void accelerate() const { cout << "Car Accelerating" << endl; }
    virtual void drive() const { cout << "Car Driving" << endl; }

  private:
    // Car inherits acceleration accessors, member
};
class Jet : public Vehicle {
  public:
    Jet() { cout << "Jet Constructor" << endl; }
    virtual ~Jet() { cout << "Jet Destructor" << endl; }
    virtual void fly() const { cout << "Jet flying" << endl; }
};

class JetCar : public Car, public Jet {
  public:
    JetCar() { cout << "JetCar Constructor" << endl; }
    virtual ~JetCar() { cout << "JetCar Destructor" << endl; }
    virtual void drive() const { cout << "JetCar driving" << endl; }
    virtual void fly() const { cout << "JetCar flying" << endl; }
};
void analyzeCarPerformance(Car *testVehicle) {
    testVehicle->drive();
    // drive() exists for both base and sub class
}
void analyzeJetPerformance(Jet *testVehicle) {
    testVehicle->fly();
    // fly() exists for both base and sub class
}

int main() {
    Car myCar;
    Jet myJet;
    JetCar myJetCar;

    cout << endl;
    cout << "Car testing in progress" << endl;
    analyzeCarPerformance(&myCar);
    analyzeCarPerformance(&myJetCar);
    cout << "Jet testing in progress" << endl;
    analyzeJetPerformance(&myJet);
    analyzeJetPerformance(&myJetCar);
    cout << endl;

    return 0;
}
```

### Outputs

- `myCar` Constructor
  ```
  Vehicle Constructor
  Car Constructor
  ```

- `myJet` Constructor
  ```
  Vehicle Constructor
  Jet Constructor
  ```

- `myJetCar` Constructor
  ```
  Vehicle Constructor
  Car Constructor
  Vehicle Constructor
  Jet Constructor
  JetCar Constructor
  ```

- `myJetCar` Destructor
  ```
  JetCar Destructor
  Jet Destructor
  Vehicle Destructor
  Car Destructor
  Vehicle Destructor
  ```

- `myJet` Destructor
  ```
  Jet Destructor
  Vehicle Destructor
  ```

- `myCar` Destructor
  ```
  Car Destructor
  Vehicle Destructor
  ```

```mermaid
---
title: Relationship between Vehicle, Car, Jet, JetCar
---
classDiagram
    note "Author: 1chooo"
    Vehicle <|-- Car: Inheritance
    Vehicle <|-- Jet: Inheritance
    Car <|-- JetCar : Inheritance
    Jet <|-- JetCar : Inheritance

    class Vehicle {
        +Vehicle()
        +~Vehicle()
        +void accelerate()
        +void setAcceleration(double)
        +double getAcceleration()
        -double acceleration
    }
    class Car {
        +Car()
        +~Car()
        +void accelerate()
        +void drive()
    }
    class Jet {
        +Jet()
        +~Jet()
        +void fly()
    }
    class JetCar {
        +JetCar()
        +~JetCar()
        +void drive()
        +void fly()
    }

```

- `JetCar` inherits from both `Car` and `Jet`. 
- `JetCar` inherits two `Vehicle` parts. This means that when calling a method that is in `Vehicle`, but not overridden in the subclass `JetCar`, or when we access a variable that exists only in `Vehicle`, 

> [!IMPORTANT]
> we must explicit specify which `Vehicle` part we are accessing: we must explicit specify which `Vehicle` part we are accessing: 


with multiple inheritance a subclass is a kind of each of its base classes. `JetCar` is a `Car` and it is a `Jet`. It may be used in places that expect a `Car` object, such as `analyzeCarPerformance()`. It can also be used in places that expect a Jet, such as `analyzeJetPerformance()`. 

However, how about the ambiguity?

## Analysis of the Ambiguity

Ambiguity can happen when you use multiple inheritance

### Solution 1: Casting Ambiguous Attributes or Methods

```cpp
class task {
    // ...
    virtual debug_info *get_debug();
};
class Displayed {
    // ...
    virtual debug_info *get_debug();
};
class Satellite : public task, public displayed {
    // ...
};
void print_debugging(Satellite *sp) {

    debug_info *dip = sp->get_debug();              // wrong
    debug_info *dip = sp->Task::get_debug();
    debug_info *dip = sp->Displayed : get_debug();
}
```

### Solution 2: Overwriting Ambiguous Attributes or Methods

```cpp
class Satellite : public Task, public Displayed {
    // ...

    // write a new function to merge the debugging messages from two sources
    debuLinfo *get_debug() {
        debug_info *dip1 = Task::get_debug();
        debug_info *dip2 = Displayed::get_debug();
        return dip->merge(dip2);
    };
};
```

### Another Case: JetCar

```cpp
class Link {
    Link * next ;
};
class Task: public Link {
     // using link to maintain a list of tasks
};
class Displayed: public Link {
     // use link to maintain a list of displayed object
};
```

```cpp
void mess_with_links(Satellite *p) {
    p->next = 0;                  // wrong
    p->Link::next;                // wrong
    p->Task::Link::next = 0;      // OK
    p->Displayed::Link::next = 0; // OK
}
```

### Another Case: Storable

想像 storable 是一個能自檔案讀出自己、將自己寫回檔案的物件


```cpp
class Storable {
  public:
    virtual const char *get_file() = 0;
    virtual void read() = 0;
    virtual void write() = 0;
    virtual ~Storable(){};
};
class Transmitter : public Storable {
  public:
    void write();
    // ...
};
class Receiver : public Storable {
  public:
    void write();
    // ...
};
class Radio : public Transmitter,
              public Receiver {
  public:
    const char *get_file();
    void read();
    void write();
    // ...
};
```

```cpp
void Radio ::write() {
    Transmitter::write();
    Receiver::write();
    // begin to write something that is really related to radio
}
```

> [!WARNING]
> 當有 `Storable(const char *s);` 有這樣的改變，下面的 radio 繼承就會出問題，會有兩份基底，但是一個 radio 不可能存到兩份 file
> ```cpp
> class Storable {
>   public:
>     Storable(const char *s); // 每一個 storable 用一個 file 來記錄
>     virtual const char *get_file() = 0;
>     virtual void read() = 0;
>     virtual void write() = 0;
>     virtual ~Storable(){};
> 
>   private:
>     const char *store;
>     Storable(const Storable &);
>     Storable &operator=(const Storable);
> };
> ```
> 
> ```cpp
> class Radio : public Transmitter, public Receiver {
>   public:
>     //...
> }
> ```

#### Diamond-Shaped Inheritance

**`public virtual`** inheritance

```cpp
class transmitter : public virtual Storable {
  public:
    void write();
};
class Receiver::public virtual Storable {
  public:
    void write();
};
class Radio : public Transmitter, public Receiver {
  public:
    void write();
};
```

```mermaid
---
title: Diamond-Shaped Inheritance
---
classDiagram
    note "Author: 1chooo"
    Receiver --> Storable
    Transmitter --> Storable
    Radio --> Transmitter
    Radio --> Receiver
```

### Java Interface 

- Java think ambiguity problem caused by multiple inheritance is too complicated.
- Most C++ programmers have problems to understand
- **Java prohibits multiple inheritance**
- BUT, it introduce interface

Suppose you already write a class

```java
Class myLinkedList extend LinkedList {
    void appendTail(node o) ;
    void appendHead(node o);
    void appendMiddle(node left, node right);
}
```

How do you make your `myLinkedList` be used as `Stack`, `Queue`

```java
Interface Stack {
    item pop();
    void push(o);
};

Interface Queue {
    enqueue(o);
    item dequeue();
}
```

The above `Stack` in C++ has virtual functions for the objects in the `Stack`.

```cpp
class Stack {
    virtual void push() = 0;
    virtual void pop() = 0;
};
```

<code>Class myLinkedList extend LinkedList <b>implement</b> <i>Stack, Queue</i></code>


```java
Class myLinkedList extend LinkedList implement Stack, Queue
    void appendTail(node o) ;
    void appendHead(node o);
    void appendMiddle(node left, node right);
    pop() { ... }
    push() { ... }
    enqueue() { ... }
    dequeue() { ... }
}
```

#### How to use Java interface?

Somewhere in initialization code

```java
Stack s = new myLinkedList();
```

Somewhere in core 

```java
s.push(o);
...
o = s.pop();
```

#### Discussion of Java Multiple Inheritance

To understand Java interface, it is better understood from multiple inheritance. 

> [!NOTE]
> Implement is a concept of purified multiple inheritance

However, how about the inheritance Principle

<code>Class A:  <i>B, C</i></code>
- **(YES)** A is B ?
- **(YES)** A is C ?

<code>Class A extend B <b>implement</b> <i>C, D</i></code>
- **(YES)** A is B ?
- **(YES or NO ???)** A is C ?
- **(YES or NO ???)** A is D ?

> [!NOTE]
> We want to change the concept of **"A is a B?"** for inheritance in Java. When we use "implement", it becomes difficult to determine. Therefore, we need to change the concept to **"A can be B?"** which represents a more flexible inheritance relationship.
>
> 我們要改變原有判定繼承的概念 **"A is a B?"** "is a" 在 Java 當我們用 Implement 我們會很難判定，因此我們會需要把觀念換成 **"A can be B?"** 我們可以想成是比較寬鬆的繼承關係。

However, think of the follow usage:

```java
Stack s = new MyLinkedList();
```

- `MyLinkedList` is a `Stack`? 

不完全是，`MyLinkedList` 只是因為可以使用 `Stack` 的元件，所以從 `Stack` 繼承過來，但是 `MyLinkedList` 並不是 `Stack`。


#### To simulate interface in C++

```cpp
Class human {
    virtual void walk() = 0;
    virtual void breath() = 0;
}
```


