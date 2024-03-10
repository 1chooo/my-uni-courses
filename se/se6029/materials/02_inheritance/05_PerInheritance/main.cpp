#include <iostream>

using namespace std;

class pet {

  public:
    pet() { cout << "pet constructor" << endl; }
    ~pet() { cout << "pet destructor" << endl; }
    void speak() { cout << "Growl " << endl; }
};

class cat : public pet {

  public:
    cat() { cout << "cat constructor" << endl; }
    ~cat() { cout << "cat destructor" << endl; }
    void speak() { cout << "meow" << endl; }
};


int main() {
    pet insect;
    cat pussy;
    pet *nose = (pet *)new cat();

    insect.speak();
    pussy.speak();
    ((pet)pussy).speak();
    nose->speak();

    return 0;
}

/*
Output:

pet constructor
pet constructor
cat constructor
pet constructor
cat constructor
Growl 
meow
Growl 
pet destructor
Growl 
cat destructor
pet destructor
pet destructor
*/
