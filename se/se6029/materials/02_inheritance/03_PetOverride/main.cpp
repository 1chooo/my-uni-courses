#include <cstdlib>
#include <iostream>

using namespace std;

class Pet {
  public:
    // Constructors, Destructors
    Pet() : weight(1), food("Pet Chow") {}
    Pet(int w) : weight(w), food("Pet Chow") {}
    Pet(int w, string f) : weight(w), food(f) {}
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
    Rat(int w) : Pet(w) {}
    Rat(int w, string f) : Pet(w, f) {}
    ~Rat() {}
    // Other methods
    void sicken() {
        cout << "Spreading Plague" << endl;
    }
};

class Cat : public Pet {
  public:
    Cat() : numberToes(5) {}
    Cat(int w) : Pet(w), numberToes(5) {}
    Cat(int w, string f) : Pet(w, f), numberToes(5) {}
    Cat(int w, string f, int toes) : Pet(w, f), numberToes(toes) {}
    ~Cat() {}
    // Other accessors
    void setNumberToes(int toes) { numberToes = toes; }
    int getNumberToes() { return numberToes; }

  private:
    int numberToes;
};

int main() {
    Rat charles(25, "Rat Chow");
    Rat john; // Default Rat constructor
    Cat fluffy(10, "rats");
    Cat buffy(10, "fish", 6);

    cout << "Charles weighs " << charles.getWeight() << " lbs. " << endl;
    charles.speak();
    charles.eat();
    charles.sicken();

    cout << "John weighs " << john.getWeight() << " lbs. " << endl;
    john.speak();
    john.eat();
    john.sicken();

    fluffy.speak();
    fluffy.eat();
    cout << "Fluffy has " << fluffy.getNumberToes() << " toes " << endl;

    buffy.speak();
    buffy.eat();
    cout << "Buffy has " << buffy.getNumberToes() << " toes " << endl;

    return 0;
}

/*
Output:

Charles weighs 25 lbs. 
Growl
Eating Rat Chow
Spreading Plague
John weighs 1 lbs. 
Growl
Eating Pet Chow
Spreading Plague
Growl
Eating rats
Fluffy has 5 toes 
Growl
Eating fish
Buffy has 6 toes
*/
