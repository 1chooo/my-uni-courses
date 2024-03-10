// main.cpp

#include "Car.h"

Car honda;

int main() {
    Car camery;
    honda.color = 1;
    camery.color = 100;

    return 0;
}

/*
Output

Car is constructed!
Car is constructed!
Car is destroyed!
Car is destroyed!

So, when is Honda’s destructor is called

Ans:
after the main program
There is a piece of code after main() to handle the globally allocated objects
*/
