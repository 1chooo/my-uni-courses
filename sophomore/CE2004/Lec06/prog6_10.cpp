#include <iostream>
#include <cstdlib>

using namespace std;

static int a;

void odd (void);

int main (void)
{
    odd();

    cout << "After odd(), a=" << a << endl;

    system("pause");

    return 0;
}

void odd (void)
{
    a = 10;

    if (a % 2 == 1)
        cout << "a=" << a << ", a is odd number." << endl;
    else
        cout << "a=" << a << ", a is even number." << endl;

    return;
}