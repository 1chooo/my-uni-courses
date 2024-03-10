// Car.cpp

#include "Car.h"
#include <iostream>

using namespace std;

Car::Car() {
    cout << "Car is constructed" << endl;
}

Car::~Car() {
    cout << "Car is destroyed!" << endl;
}
