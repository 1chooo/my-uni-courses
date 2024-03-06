#include "Dog.h"
#include <iostream>

using namespace std;

void Dog::setAge(int age) {
    this->age = age;
}

int Dog::getAge() {
    return age;
}

void Dog::setWeight(int weight) {
    this->weight = weight;
}

int Dog::getWeight() {
    return weight;
}

void Dog::speak() {
    cout << "BARK!!" << endl;
}
