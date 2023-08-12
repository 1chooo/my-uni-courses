// implicit type conversion

#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int a = 36, b = 7;

    cout << "a=" << a << "b=" << b << ", ";
    cout << "a/b=" << (a / b) << endl;
    cout << "a=" << a << "b=" << b << ", ";
    cout << "a/b=" << (float) a / b << endl;    // this only convert the type of a

    system("pause");

    return 0;
}