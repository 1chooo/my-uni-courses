#define MAXCAPACITYINROOM 50

#include <iostream>

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
    int quit = 0;
    int choice;
    int totalNumber;
    Pet *house[MAXCAPACITYINROOM]; // Array of pointers to base class
    int i = 0;
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
    totalNumber = i;
    for (i = 0; i < totalNumber; i++) {
        house[i]->speak();
    }
    return 0;
}
