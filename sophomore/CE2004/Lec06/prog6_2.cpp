#include <iostream>
#include <cstdlib>

using namespace std;

int square (int a)
{
    int squ;
    squ = a * a;

    return squ;
}

int main (void)
{
    cout<< "square(6)=" << square(6) << endl;

    system("pause");

    return 0;
}