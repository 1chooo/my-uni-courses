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
    void speak();
};

void Rat::speak() { cout << "Rat noise" << endl; }

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

    // Other methods
    void speak();

  private:
    int numberToes;
};

void Cat::speak() { cout << "Meow" << endl; }

int main() {
    Pet peter;
    Rat ralph;
    Cat chris;

    peter.speak();
    ralph.speak();
    chris.speak();

    return 0;
}

/*
Output:

Growl
Rat noise
Meow
*/
