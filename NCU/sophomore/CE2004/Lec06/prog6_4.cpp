#include <iostream>
#include <cstdlib>

using namespace std;

int max (int, int);

int main (void)
{
    int a = 12, b = 35;
    cout << "a=" << a << ", b=" << b << endl;
    cout << "The large number is " << max(a, b) << endl;

    system("pause");

    return 0;
}

int max (int i, int j)
{
    if (i > j)
        return i;
    else
        return j;
}