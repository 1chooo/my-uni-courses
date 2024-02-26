#include <iostream>
#include "Cat.h"

int main() {
    // Single Argument form of array initialization list
    // Cat myCats[4] = {"Homer", "Marge", "Bart", "Lisa"};
    Cat myCats[4] = {
        Cat("Homer"),
        Cat("Marge"),
        Cat("Bart"),
        Cat("Lisa")
    };

    // Emplicit use of constructors in array initialization list
    Cat myOtherCats[3] = {
        Cat("Chris", "Gray"),
        Cat("Charles", "White"),
        Cat("Cindy", "BlueGray")
    };
    
    Cat *catpt = new Cat[27];
    Cat *pt;
    // Use accessor methods to initialize dynamically allocated class objects
    pt = catpt;
    for (int i = 0; i < 27; i++) {
        pt->setName("Felix");  // You can never have enough
        pt->setColor("Black"); // black cats named Felix
        pt++;                  // Can also increment pointer within the for statement
    }

    return 0;
}
