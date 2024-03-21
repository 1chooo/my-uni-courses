#include <iostream>
#include <vector>

using namespace std;

class Animal {
  public:
    virtual void speak() = 0;
    virtual ~Animal() {}
};

class Cat : public Animal {
  public:
    void speak() {
        cout << "meow" << endl;
    }
};

class Cow : public Animal {
  public:
    void speak() {
        cout << "moo" << endl;
    }
};

int main(void) {
    vector<Animal *> animals = {new Cat(), new Cow()};
    for (Animal *animal : animals) {
        animal->speak();
    }

    for (Animal *animal : animals) {
        delete animal;
        animal = nullptr;
    }
    animals.clear();

    return 0;
}