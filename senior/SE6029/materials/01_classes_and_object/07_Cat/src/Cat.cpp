#include "Cat.h"
#include <iostream>

Cat::Cat(
    std::string name,
    std::string color) : _name(name), _color(color) {}

/*
 * We can also announce the Cat Constructor in
 * this way without using the `NameList`
 * Cat::Cat(
 *  std::string name,
 *  std::string color) {
 *    _name = name;
 *   _color = color;
 * }
 */

Cat::~Cat() {}

void Cat::setName(std::string name) {
    _name = name;
}

std::string Cat::getName() {
    return _name;
}

void Cat::setColor(std::string color) {
    _color = color;
}

std::string Cat::getColor() {
    return _color;
}

void Cat::speak() {
    std::cout << "meow" << std::endl;
}
