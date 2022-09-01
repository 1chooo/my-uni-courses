#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int a, b = 5;
    double c = 3.14;

    cout << "a=" << a << ", sizeof(a)=" << sizeof(a);
    cout << ", the address is: " << &a << endl;
    cout << "b=" << b << ", sizeof(b)=" << sizeof(b);
    cout << ", the address is: " << &b << endl;
    cout << "c=" << c << ", sizeof(c)=" << sizeof(c);
    cout << ", the address is: " << &c << endl;

    system("pause");

    return 0;
}