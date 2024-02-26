#include "Table.h"
#include <iostream>

Table::Table(int s) {
    p = new char[100];
    sz = s;
    std::cout << "constructor" << std::endl;
}

Table::~Table() {
    delete[] p;
    std::cout << "destructor" << std::endl;
}
