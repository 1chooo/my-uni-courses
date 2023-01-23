#include <iostream>
#include <cstdlib>

using namespace std;

int main(void)
{
    int a = 10, &ref = a;
    int b = 15, *ptr;

    ptr = &b;

    cout << a << "+" << b << "=";
    cout << ref + *ptr << endl;

    system("pause");

    return 0;
}