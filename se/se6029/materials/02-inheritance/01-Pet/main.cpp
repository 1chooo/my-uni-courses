#include <cstdlib>
#include <iostream>

using namespace std;

class Pet {
  public:
    // Constructors, Destructors
    Pet() : weight(1), food("Pet Chow") {}
    ~Pet() {}
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
    Rat() {}
    ~Rat() {}
    // Other methods
    void sicken() {
        cout << "Spreading Plague" << endl;
    }
};

class Cat : public Pet {
  public:
    Cat() : numberToes(5) {}
    ~Cat() {}
    // Other accessors
    void setNumberToes(int toes) { numberToes = toes; }
    int getNumberToes() { return numberToes; }

  private:
    int numberToes;
};

int main() {
    Rat charles;
    Cat fluffy;

    charles.setWeight(25);
    cout << "Charles weighs " << charles.getWeight() << " lbs. " << endl;
    charles.speak();
    charles.eat();
    charles.sicken();

    fluffy.speak();
    fluffy.eat();
    cout << "Fluffy has " << fluffy.getNumberToes() << " toes " << endl;
    
    return 0;
}


/*
Output:

Charles weighs 25 lbs. 
Growl
Eating Pet Chow
Spreading Plague
Growl
Eating Pet Chow
Fluffy has 5 toes
*/
