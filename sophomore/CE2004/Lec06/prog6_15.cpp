#include <iostream>
#include <cstdlib>

using namespace std;

int power (int, int);

int main (void)
{
    int a = 2, b = 3;

    cout << a << "^" << b << "=";
    cout << power(a, b) << endl;

    system("pause");

    return 0;
}

int power (int a, int b)
{
    if (b == 0)
        return 1;
    else 
        return (a * power(a, b - 1));
}