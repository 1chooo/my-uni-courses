#include <iostream>

class Base {
  public:
    virtual void foo() const {
        std::cout << "A's foo!" << std::endl;
    }
};

class Derived : public Base {
  public:
    virtual void foo() const {
        std::cout << "B's foo!" << std::endl;
    }
};

int main() {
    Base *o1 = new Base();
    Base *o2 = new Derived();
    Derived *o3 = new Derived();

    o1->foo();
    o2->foo();
    o3->foo();

    return 0;
}
