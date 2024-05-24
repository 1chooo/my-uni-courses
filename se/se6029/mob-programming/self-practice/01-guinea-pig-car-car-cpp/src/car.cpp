// car.cpp

#include "car.h"

Car::Car() {
    speed = 0;
    initSpeed = speed;
    accelerateSpeed = 0;
}

Car::Car(int initSpeed, int accelerateSpeed) {
    speed = initSpeed;
    this->initSpeed = initSpeed;
    this->accelerateSpeed = accelerateSpeed;
}

void Car::accelerate() {
    speed = accelerateSpeed;
}

void Car::resetSpeed() {
    speed = initSpeed;
}

int Car::getSpeed() {
    return speed;
}
