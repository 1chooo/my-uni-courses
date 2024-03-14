# Material 03 - PolyMorphism

Polymorphism in C++ is exhibited by the ability of a pointer or reference to a base class type to behave in different ways when it is used to manipulate objects of different subtypes of that base class. 

多形就是當你可以用基底 class 的指標或參考來進行處理時，卻可以依照其 subtype 來進行不一樣的事情（其實多形是很難用解釋的）

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
