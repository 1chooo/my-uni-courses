#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int a = 100, b = 15;
    cout << "a=" << a << ", b=" << b << endl;

    a -= b;
    cout << "after a-=b, a=" << a << ", b=" << b << endl;

    system("pause");

    return 0;
}