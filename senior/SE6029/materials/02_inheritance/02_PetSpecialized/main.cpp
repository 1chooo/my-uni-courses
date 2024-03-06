#include <cstdlib>
#include <iostream>

using namespace std;

class Pet {
  public:
    // Constructors, Destructors
    Pet() : weight(1), food("Pet Chow") {
        cout << "Pet Constructor" << endl;
    }
    ~Pet() {
        cout << "Pet Destructor" << endl;
    }
    // Accessors
    void setWeight(int w) { weight = w; }
    int getWeight() { return weight; }
    void setfood(string f) { food = f; }
    string getFood() { return food; }
    // General methods
    void eat();
    void speak();

  protected: // subclasses can access these
    int weight;
    string food;
};

void Pet::eat() {
    cout << "Eating " << food << endl;
}

void Pet::speak() {
    cout << "Growl" << endl;
}

// use inheritance to solve the reused problem

class Rat : public Pet {
  public:
    Rat() { cout << "Rat Constructor" << endl; }
    ~Rat() { cout << "Rat Destructor" << endl; }
    // Other methods
    void sicken() {
        cout << "Spreading Plague" << endl;
    }
};

class Cat : public Pet {
  public:
    Cat() : numberToes(5) { cout << "Cat Constructor" << endl; }
    ~Cat() { cout << "Cat Destructor" << endl; }
    // Other accessors
    void setNumberToes(int toes) { numberToes = toes; }
    int getNumberToes() { return numberToes; }

  private:
    int numberToes;
};

int main() {
    Rat charles;
    Cat fluffy;
    // charles.setWeight(25);
    // cout << "Charles weighs " << charles.getWeight() << " lbs. " << endl;
    // charles.speak();
    // charles.eat();
    // charles.sicken();
    // fluffy.speak();
    // fluffy.eat();
    // cout << "Fluffy has " << fluffy.getNumberToes() << "toes " << endl;
    return 0;
}

/*
Output:

Pet Constructor    // Charles Pet Constructor
Rat Constructor    // Charles Rat Constructor
Pet Constructor    // Fluffy Pet Constructor
Cat Constructor    // Fluffy Cat Constructor
Cat Destructor     // Fluffy Cat Destructor
Pet Destructor     // Fluffy Pet Destructor
Rat Destructor     // Charles Rat Destructor
Pat Destructor     // Charles Pat Destructor
*/
