// guinea_pig_car_car.cpp

#include "guinea_pig_car_car.h"
#include <iostream>

GuineaPigCarCar::GuineaPigCarCar() : GuineaPig("GuineaPigCarCar"), car(), foods() {}

GuineaPigCarCar::GuineaPigCarCar(std::string name, Car car) : GuineaPig(name), car(car), foods() {}

void GuineaPigCarCar::eat(std::string food) {
    std::cout << name << " eat " << food << std::endl;
    eatRule(food);
}

void GuineaPigCarCar::pupu() {
    std::cout << name;
    for (const auto &pupu : foods) {
        std::cout << " " << pupu;
    }
    std::cout << std::endl;
    foods.clear();
    foodCount = 0;

    car.resetSpeed();
}

int GuineaPigCarCar::getSpeed() {
    return car.getSpeed();
}

void GuineaPigCarCar::eatRule(std::string food) {
    foods.push_back(food);

    if (foods.size() > 5) {
        car.resetSpeed();
    } else if (food == "carrot") {
        car.accelerate();
    } else {
        // do nothing
    }
}
