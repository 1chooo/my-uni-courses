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

/*
Pet Created
Pets singing
Growl
Growl
Growl

Rat Created
Rats singing
Growl
Rat noise
Rat noise

Cat Created
Cats singing
Growl
Meow
Meow
*/