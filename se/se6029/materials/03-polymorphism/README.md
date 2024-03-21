# Material 03 - PolyMorphism    <!-- omit from toc --> 

Polymorphism in C++ is exhibited by the ability of a pointer or reference to a base class type to behave in different ways when it is used to manipulate objects of different subtypes of that base class. 

多形就是當你可以用基底 class 的指標或參考來進行處理時，卻可以依照其 subtype 來進行不一樣的事情（其實多形是很難用解釋的）

**Table of Contents:**
- [Using a graphics application](#using-a-graphics-application)
- [Virtual function](#virtual-function)
  - [Object Slicing](#object-slicing)
  - [Discussion `chorus` function](#discussion-chorus-function)
    - [Pass by value](#pass-by-value)
    - [Pass by pointer](#pass-by-pointer)
    - [Pass by reference](#pass-by-reference)
- [Core Concept of Object-Oriented Programming](#core-concept-of-object-oriented-programming)
- [OOP (The Four Basic Elements)](#oop-the-four-basic-elements)
  - [Making PolyMorphism without OOP](#making-polymorphism-without-oop)
  - [How we can make it better?](#how-we-can-make-it-better)
  - [function pointer](#function-pointer)
    - [Making PloyMorphism with OOP](#making-ploymorphism-with-oop)
  - [Static Linking of External References in C Language](#static-linking-of-external-references-in-c-language)
    - [Indirect CALL \[^1\]](#indirect-call-1)
  - [Dynamic Binding](#dynamic-binding)
    - [Virtual Function Table of Derived Classes](#virtual-function-table-of-derived-classes)
    - [Virtual Base Class (Abstract class)](#virtual-base-class-abstract-class)
    - [Questions](#questions)
- [One Critical Point to Determine if you OO program is really doing right](#one-critical-point-to-determine-if-you-oo-program-is-really-doing-right)

## Using a graphics application

Suppose we have a base class called "shape", many shapes are derived from it, such as "box", "circle", "rectangle" and so on. 

In this type of application, it is inevitable you encounter such fragment of code to repaint all objects

Suppose all the objects are put in a `vector<shape *>container`

```cpp
void paintall(vector<shape *> & container) { 
for each shape object x  in container 
     x->draw(); 
}
```

In this example, we hope each object can draw its specific shapes.

> [!NOTE]
> 我們可不希望前一堂課的按照 pointer 類別呼叫 method 的狀況出現

<div align="right">
    <a href="#material-03---polymorphism">Back to top</a>
</div>

## Virtual function

```cpp
class Pet {
  public:
    // Constructors, Destructors
    Pet() {}
    virtual ~Pet() {}
    // General methods
    virtual void speak();
    void breath();
};
```

- 任何想要被繼承的 class，overridden 的 method 都要宣告成 virtual
- 一個 function 一旦宣告成 virtual，則在繼承的 class 中也是 virtual。但是可以忽略不寫，不過建議要寫！
- Polymorphism only works for pointer and reference with function that declared as virtual
- If a class has any method declared as virtual, its destructor should be declared as virtual.

> [!NOTE]
> The method, `breath()`, is not declared as virtual. Why? 
> 
> Because I am assuming that all animals breath and that this method will not be overridden in base classes.
> 
> Suppose that later some programmer defines a "fish" subclass. Then, perhaps, breath needs to be **overridden** to allow for underwater breathing. For now, I'll assume it's adequate. 


Why not declare all methods as virtual? 
- This could be done, but involves additional overhead. The compiler creates a virtual function table that is used in the polymorphism mechanism. Avoiding unnecessary details, the more functions that are declared as virtual, the greater the overhead to create and maintain these tables. 
- But, by declaring all methods virtual, redesign may be avoided if the classes need to change. 

Some C++ programmers declare all methods virtual if any need be. Some don't. In some programming languages, such as Java, **all methods are virtual by default**. I don't have a definitive answer on this one.

```cpp
#include <iostream>
#include <string>

using namespace std;

class Pet {
  public: // Constructors, Destructors
    Pet() {}
    virtual ~Pet() {}
    // General methods
    virtual void speak();
    void breath() { cout << "Gasp" << endl; }
};

void Pet::speak() { cout << "Growl" << endl; }

class Rat : public Pet {
  public:
    Rat() {}
    ~Rat() {}
    void speak();
};

void Rat::speak() { cout << "Rat noise" << endl; }

class Cat : public Pet {
  public:
    Cat() {}
    ~Cat() {}
    void speak();
};

void Cat::speak() { cout << "Meow" << endl; }

void chorus(Pet pet, Pet *petPtr, Pet &petRef) {
    pet.speak();
    petPtr->speak();
    petRef.speak();
}

int main() {
    Pet *ptr; // Pointer to base class

    ptr = new Pet;
    cout << "Pet Created" << endl;
    cout << "Pets singing" << endl;
    chorus(*ptr, ptr, *ptr);
    cout << endl;
    delete ptr; // Prevent memory leaks

    ptr = new Rat;
    cout << "Rat Created" << endl;
    cout << "Rats singing" << endl;
    chorus(*ptr, ptr, *ptr);
    cout << endl;
    delete ptr; // Prevent memory leaks

    ptr = new Cat;
    cout << "Cat Created" << endl;
    cout << "Cats singing" << endl;
    chorus(*ptr, ptr, *ptr);
    cout << endl;
    delete ptr; // Prevent memory leaks

    return 0;
}
```

### Object Slicing

In this example, the compiler makes space for a `Pet` object and then copies the `Rat` object argument into it. Since the `Rat` object is **larger**, it doesn't fit. This is called slicing. Only the `Pet` part of `Rat` gets copied. When speak is called, it is Pet's speak method that is executed.

```
+----------+ 
|    Pet   | 
+----------+ 
|  Rat(x)  |  -> slice
+----------+ 
```

### Discussion `chorus` function

```cpp
void chorus(
    Pet pet,            // Pass by value
    Pet *petPtr,        // Pass by pointer
    Pet &petRef         // Pass by reference
) {
    pet.speak();
    petPtr->speak();    // Also (*petPtr).speak(); dereference
    petRef.speak();
}
```

#### Pass by value

When passing an argument by value, a copy is made.

```
+--------+ 
|  Pet   | -> Pet pet
+--------+ 
|  Rat   | 
+--------+ 
```

#### Pass by pointer

pass the address

```
+--------+ init address -> Pet &petRef
|  Pet   |
+--------+ 
|  Rat   | 
+--------+ 
```

#### Pass by reference

pass the reference

```
+--------+ init address -> Pet *petPtr 
|  Pet   |
+--------+ 
|  Rat   | 
+--------+ 
```

When passed a pointer of type `Pet` holding the address of a `Rat` object, we get `Rat` behavior - "rat noise" is printed. This is polymorphism.

> [!NOTE]
> Polymorphism is seen when a pointer or reference of a base class points to a subclass object. Methods must be declared as `virtual` for polymorphism to work.



## Core Concept of Object-Oriented Programming

> [!IMPORTANT]
> Object-oriented programming is about pushing the core parts outward and encapsulating the changing parts, such as future extensions and additions.

**Extension part:** In the future, we can add the dog, elephant, and other animals. 

```cpp
class Pet {
  public: // Constructors, Destructors
    Pet() {}
    virtual ~Pet() {}
    // General methods
    virtual void speak();
    void breath() { cout << "Gasp" << endl; }
};

void Pet::speak() { cout << "Growl" << endl; }

class Rat : public Pet {
  public:
    Rat() {}
    ~Rat() {}
    void speak();
};

void Rat::speak() { cout << "Rat noise" << endl; }

class Cat : public Pet {
  public:
    Cat() {}
    ~Cat() {}
    void speak();
};

void Cat::speak() { cout << "Meow" << endl; }

void chorus(Pet pet, Pet *petPtr, Pet &petRef) {
    pet.speak();
    petPtr->speak();
    petRef.speak();
}
```

**UI Part:** This is the part that we will make change constantly. 

```cpp
while (!quit && i < MAXCAPACITYINROOM) {
    cout << "Enter (0) to quit" << endl;
    cout << "Enter (1) for Rat" << endl;
    cout << "Enter (2) for Cat" << endl;
    cin >> choice;
    if (choice == 0) {
        quit = 1;
    } else if (choice == 1) {
        house[i++] = new Rat();
    } else if (choice == 2) {
        house[i++] = new Cat();
    } else {
        cout << "Invalid Choice, Reenter" << endl;
    }
}
```

**Core Code Part:** In the future, this is the part that we will keep in the orginal program. 

```cpp
while() {
    ...
    else {
        cout << "Invalid Choice, Reenter" << endl;
    }
}
totalNumber = i;
for (i = 0; i < totalNumber; i++) {
    house[i]->speak();
}
```

We chosen an array of pointers of the base class type, "Pet", to store my pets as I enter them into the program. Because We do not know at compile time the type of each subclass object (Rat or Cat) and need to be able to store either. 

> [!IMPORTANT]
> We need each to behave as the subclass it is. We want **polymorphism**. That is, I want each object to have the appropriate behavior according to its subclass. 

> [!TIP]
> An array of objects would not work. Remember, polymorphism is supported through pointers and references. 

## OOP (The Four Basic Elements)

- Object and Class (Data and Methods)
- Inheritance (Base and Derived Class)
- Encapsulation (`public`, `protected`, `private`)
- Polymorphism (Dynamic Binding)

In object-oriented languages, polymorphism is a natural result of combining inheritance and message passing.

> [!IMPORTANT] 
> What is polymorphism?
> - Polymorphism refers to the ability of a function to automatically perform different operations and functionalities based on the type or object it is dealing with.
> Unlike overloading, polymorphism allows **the same block of code** to be used to operate on different data types or objects.

### Making PolyMorphism without OOP

```c
Color newColor;     // Currecnt drawing color

void main() {
    int Cont = 1;   // Continue flag
    int Event = 0;  // Event code

    if (Initial()) {    // Enter the drawing mode and other settings
        while (Cont) {
            Event = GetEvent(); // Get the event code
            switch (Event) {    // Determine the event code
                case Circle:
                case Pie:
                case Ellipse:
                case EllipsePie:
                    gCircle(Event, NowColor); // if circle function related, call gCircle function
                    break;
                case Rect:
                case RoundRect:
                case Box:
                    gRect(Event, NowColor); // if rectangle function related, call gRect function
                    break;
                ...

                case Exit:
                    Cont = !gExit();    // if exit function related, call gExit function
                    break;
            }
        End();      // Release memory and exit the drawing mode
        }
    }
}
```

Switch Patterns often appear in several places in the program. This is a sign that the program is not well designed.

If we modify one of the functions, we need to modify every switch statement in the program which means we need to realize the whole detail of the program.

### How we can make it better?

```
+----------+----------+----------+----------+
| Module 1 | Module 2 | Module 3 | Module 4 |  (Here We don't need to change !)
+----------+----------+----------+----------+
|               Pet Interface               |
+-------------------------------------------+ 
                    ^
                    |
         Dog, Rat, Cat, Elephant, ...
```

### function pointer

define the function to store the pointer of the function

```c
int (*f)(int, int);
int (*f[])(int,int);
```

```c
Color newColor;
int Cont = 1;

void main() {
    int E = 0;
    struct {
        int (*Draw) (void (*)(), void (*)());
        void (*Move);
        void (*Act);
    } F[] = {
        {gRegion, XorCircle, PutCircle},
        {gRegion, XorCircle, PutPie},
        {gRegion, XorEllipse, PutEllipse},
        {gRegion, XorEllipse, PutEllipsePie},
        {gRegion, XorRect, PutRect},
        {gRegion, XorLine, PutBar},
        {gExit, NULL, NULL}
    };

    if (Initial()) {
        while (Cont) {
            E = GetEvent();
            (*F[E].Draw)(F[E].Move, F[E].Act);
        }
        End();
    }
}
```

> [!NOTE]
> `int (*Draw) (void (*)(), void (*)());` is a pointer to a function that takes two function pointers as arguments and returns an integer.

```c
if (Initial()) {
      while (Cont) {
          E = GetEvent();
          (*F[E].Draw)(F[E].Move, F[E].Act);
      }
      End();
  }
```

The above code is not related to extense the function of the program.


> [!IMPORTANT]
> Inheritance along cannot implement polymorphism.
> 
> -> We need a new mechanism **called dynamic binding** to make polymorphism to work.

#### Making PloyMorphism with OOP

```cpp
class Circle : Public Shape {
    public:
        virtual void Draw() { ... }
        virtual void Move() { ... }
        virtual void Act() { ... }
};

void main() {
    Vector <Shape *> shapePool;
    shapePool.insert(new Circle);
    shapePool.insert(new Pie);
    ...

    if (initial()) {
        while (cont) {
            E = GetEvent();
            shapePool[E]->Draw();
            shapePool[E]->Move();
            shapePool[E]->Act();
        }
        End();
    }
}

## What is binding?

**Original C Program:**

```c
void do_something() {
    /* */
}
void sit_on_it() {
    /* */
}
void think_it() {
    /* */
}

main() {
    float x, y, z;
    sit_on_it();
    think_it();
    do_something();
    x = y + x;
}
```

**Assembly code after compilation:**

Logical Address

```asm
    START    MAIN
do_something:
    ...
    RET
sit_on_it:
    ...
    RET
think_it:
    ...
    RET

main:
    ...
    CALL sit_on_it      // <-- Binding (compliation time binding)
    CALL think_it       // <-- Binding (compliation time binding)
    CALL do_something   // <-- Binding (compliation time binding)
    ...
    PUSH y
    PUSH z
    CALL FLOAT_PLUS   // <-- Conduct the Library (Linking time binding)
    MOVE R0, x
    END
```


### Static Linking of External References in C Language
```
  Compile Action                                Linking Action 
  --------------                                --------------

Compiled Assembly Code     External Reference Table      External Goal File
+-------------------+    +---------------------+-----+    +--------------------+ 
| main:             |    |                     |     |    |                    | 
|   CALL ExtTbl[0]; |----|---->  sit_on_it;    | (*) |    |  ($) do_something; |        
|   sit_on_it;      |    |                     |     |    |     ...            |    
|                   |    |                     |     |    |     RET            |     
|   CALL ExtTbl[1]; |----|---->  think_it;     | (^) |    |  (*) sit_on_it;    |       
|   think_it;       |    |                     |     |    |     ...            |      
|                   |    |                     |     |    |     RET            |     
|   CALL ExtTbl[2]; |----|----> do_something;  | ($) |    |  ($) think_it;     |      
|   do_something;   |    |                     |     |    |   ...              |  
+-------------------+    +---------------------+-----+    +--------------------+
   (Indirect CALL)
```

> [!NOTE]
> DDL (Dynamic Link Library) is a library that is linked to the program at runtime. 
> 
> When the operating system executes the program, it loads the specific DLL file based on the program's record. We do not know the memory address of the DLL in advance.

#### Indirect CALL [^1]

The main difference between the direct and the indirect call, is that:

- the direct call uses an instruction call with a fixed address as argument. After the linker has done its job, this address will be included in the opcode.
- the indirect call uses an instruction call with a register as argument (here rax). The register is previously loaded either directly with the fixed address of the subroutine that is to be called, or with a value fetched from somewhere else, such as another register or a place in memory where the subroutine’s address was previously stored.

As a consequence, the direct call will always call the same subroutine, whereas the indirect call could call different subroutines, depending of what was loaded in the register before the call is made. Depending on the cpu, the indirect call might be a little slower since the indirection requires an extra effort.

A typical use case for the indirect call in assembly would be to implement what would be a call to a function pointer in C or a virtual member function in C++. In your example it’s the use of the function pointer f_sub in the C source code. The key take-away here is that the same code (use of function pointer in C or indirect call in assembler) could call any C function or assembly subroutine that has the same interface and the choice is made at runtime.

The other differences between the two files are cosmetic, except for the load of the subroutine’s address into rax.

### Dynamic Binding

```cpp
class Shape {
    public:
        double x0, y0;
        Shape(double x, doubel y);
        virtual double area();
        virtual void   draw();
}
```

```
Shape Table   +--> Virtual Function Table    Practical Function
+----------+  |    +---------------------+   +-----------------+
| x0, y0   |  |    | (*area)()   --------|---|-> Shape::area() |
+----------+  |    +---------------------+   +-----------------+
| vptr; ---|--|    | (*draw)()   --------|---|-> Shape::draw() |
+----------+       +---------------------+   +-----------------+
```

#### Virtual Function Table of Derived Classes

```cpp
class Circle : Public Shape {
    public:
        double radius;
        Circle(double x, double y, double r);
        void draw();
}
```

```
Shape Table  +--> Virtual Function Table  Practical Function
+----------+ |   +---------------------+  +-----------------+
| x0, y0   | |   | (*area)()  ---------|--|-> Shape::area() |
+----------+ |   +---------------------+  +-----------------+
| vptr; ---|-|   | (*draw)()  ---------|--|-> Shape::draw() |
+----------+     +---------------------+  +-----------------+
| radius   |   <--- Circle Specific Data
+----------+  
```


```cpp
Shape *p ;
Shape A ;
Circle B ;

p = &A ;
p->draw();      // (p0<vptr[1])();  Shape object
p = &B ;
p->draw();      // (p0<vptr[1])();  Circle object
```

> [!NOTE]
> The Dynamic Compiler doesn't care whether it compiles as `p->draw();` or not, because the runtime will determine the action based on the memory content. This is the manifestation of Polymorphism.


> [!IMPORTANT]
> Actually, writing OO programs is a process, not just programming. Most programmers learn OOP (C++, Java) first, without knowing that writing OO programs require a planning and design first.
> 
> It is a process not a programming task! It's goal: to make **the system highly reusable and maintainable**

```cpp
class Circle : Public Shape{
    public:
        virtual void Draw() { ... }
        virtual void  Move() { ... }
        virtual void  Act() { ... }
};
void main () {
    Vector <Shape *>  ShapePool ;
    ShapePool.insert(new Circle);
    ShapePool.insert(new Pie);
    ...
    if (initial()) {
        while (cont) {
            E = GetEvent();
            ShapePool[E]->Draw();   // How can this be achieved?
        }
    }
}
```

Take the following examples again. When you want to extend the system to another shape called Polyghon. You simply write a class to extend Shap and add a new line in `main()` or some function called `init()` and then **you do not need to change other parts of the program.**


#### Virtual Base Class (Abstract class)

In C++, class that has member functions are pure virtual function, such as 

```cpp
virtual void p() = 0;
```

These classes are called abstract classes, which means they cannot be instantiated. In other words, you cannot create instances of these classes using the `new` keyword in your program. If you try to do so, you will encounter a compile error.

```cpp
class Human {
    public:
        virtual Money work() = 0 ;
};
```

> [!NOTE]
> If a member function can be overridden by subclass, declare it as virtual
> 
> If you like to use multiple inheritance, then whenever a class may have two or more derived classes, you should prefix the inheritance with the keyword "virtual".

#### Questions

Why not making an abstract class to have all the methods to be abstract and enforce its subclasses to implement each methods? Such as 

```cpp
class Human {
    public:
        virtual void walk() = 0 ;
        virtual void breath() = 0 ;
        virtual void speak()=0;
};
```

> [!IMPORTANT]
> In the context of polymorphism, the concept must be placed at a core part of the code. Regardless of how the system is expanded, the main code does not need to be modified. This allows the centralized part to be independent of the specific concept.


## One Critical Point to Determine if you OO program is really doing right

```cpp
class base {
    int a ;
    int b ;
}
class something : base {
    int c ;
    int d ;
}

class somethingNew : base {
    int e;
}

Somewhere in the code
...
...
...
something s = new something();   // When add somethingNew, you need to change the code
...
s.
```

In an object-oriented system, the core part should be written independent of **subtypes** or changes. This can be achieved by using Polymorphism.


[^1]: [Difference between direct and indirect function() calls](https://softwareengineering.stackexchange.com/questions/401110/difference-between-direct-and-indirect-function-calls)