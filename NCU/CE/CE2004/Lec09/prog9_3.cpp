#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int a = 5, b = 3;
    int *ptr;

    ptr = &a;
    cout << "&a=" << &a << ", ptr=" << &ptr;
    cout << ", ptr=" << ptr << ", *ptr=" << *ptr << endl;

    ptr = &b;
    cout << "&b=" << &b << ", ptr=" << &ptr;
    cout << ", ptr=" << ptr << ", *ptr=" << *ptr << endl;

    system("pause");

    return 0;
}