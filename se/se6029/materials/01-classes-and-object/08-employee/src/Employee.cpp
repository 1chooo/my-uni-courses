#include "Employee.h"
#include <cstring>

Employee::Employee(char *name, int id) {
    _id = id;
    _name = new char[strlen(name) + 1]; // add 1 for '\0' to end of string
    // Allocates an character array object
    strcpy(_name, name);
}

// 為避免 dangling pointer，我們需要在 Employee 建立 copy constructor

Employee::Employee(Employee &rhs) {
    _id = rhs.getId();
    _name = new char[strlen(rhs.getName()) + 1];
    strcpy(_name, rhs._name);
}

Employee::~Employee() {
    delete[] _name;
}

char *Employee::getName() {
    return _name;
}

int Employee::getId() {
    return _id;
}
