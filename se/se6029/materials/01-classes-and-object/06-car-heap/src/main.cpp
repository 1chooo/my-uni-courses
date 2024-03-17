// main.cpp

#include "Car.h"

Car honda;

int main() {
    Car *camery = new Car();
    honda.color = 1;
    camery->color = 100;
}

/*
Output

Car is constructed!
Car is constructed!
Car is destroyed!
*/
