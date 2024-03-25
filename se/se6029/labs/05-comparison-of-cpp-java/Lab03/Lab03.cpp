#include <iostream>

class Parent {
public:
    Parent(int x) {
        std::cout << "Parent constructor called with parameter: " << x << std::endl;
    }
};

class Child : public Parent {
public:
    Child(int y) : Parent(y) {
        std::cout << "Child constructor called with parameter: " << y << std::endl;
    }
};

int main() {
    Child childObj(10); // 建立 Child 物件時傳遞參數到父類別建構子
    return 0;
}
