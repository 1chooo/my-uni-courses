#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int *ptr, num = 20;

    ptr = &num;

    cout << "num=" << num << ", &num=" << &num << endl;
    cout << "*ptr=" << *ptr << ", ptr=" << ptr;
    cout << ", &ptr=" << &ptr << endl;

    system("pause");

    return 0;
}