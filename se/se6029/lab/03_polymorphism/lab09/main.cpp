
#include <iostream>

class base {
public:
    int x;
    int y;
    virtual void dosomething() {}
};

int main() {
    std::cout << sizeof(base) << std::endl;
    return 0;
}
