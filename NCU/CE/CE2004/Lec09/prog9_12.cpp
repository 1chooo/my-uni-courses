#include <iostream>
#include <cstdlib>

using namespace std;

int square (int);

int main (void)
{
    int (*pf)(int);
    pf = square;

    cout << "square(5)=" << (*pf)(5) << endl;

    system("pause");

    return 0;
}

int square (int a)
{
    return (a * a);
}