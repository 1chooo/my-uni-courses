#include <iostream>

using namespace std;

class Dog {
  public:
    Dog();  // Constructor
    ~Dog(); // Destructor
    void setAge(int age);
    int getAge();
    void setWeight(int weight);
    int getWeight();
    void speak();

  private:
    int age;
    int weight;
};

Dog::Dog() {
    age = 0;
    weight = 0;
    cout << "Dog Constructor Called" << endl;
}

Dog::~Dog() {
    cout << "Dog Destructor Called" << endl;
}
