// guinea_pig.cpp

#include "guinea_pig.h"
#include <iostream>

GuineaPig::GuineaPig() : name("GuineaPig"), foodCount(0) {}

GuineaPig::GuineaPig(std::string name) : name(name), foodCount(0) {}

void GuineaPig::noise() {
    std::cout << name << " PuiPui." << std::endl;
}

void GuineaPig::eat(std::string food) {
    std::cout << name << " eat " << food << std::endl;
}

void GuineaPig::pupu() {
    std::cout << name << " pupu." << std::endl;
    foodCount = 0;
}

std::string GuineaPig::getName() {
    return name;
}
