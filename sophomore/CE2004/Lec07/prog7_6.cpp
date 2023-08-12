#include <iostream>
#include <cstdlib>

using namespace std;

int add (int, int);
double add (double, double);

int main (void)
{
    iint a = 10; b = 20;
    double x = 2.3, y = 3.5;

    cout << a << "+" << b << "=" << add(a, b) << endl;
    cout << x << "+" << y << "=" << add(x, y) << endl;

    system("pause");

    return 0;
}

int add (int i, int j)
{
    return i + j;
}

double add (double i, double j)
{
    return i + j;
}