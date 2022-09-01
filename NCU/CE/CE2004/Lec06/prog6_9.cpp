#include <iostream>
#include <cstdlib>

using namespace std;

void peri (double), area (double);

int main (void)
{
    extern double PI;
    double r = 1.0;

    cout << "PI=" << PI << endl;
    cout << "radius=" << r << endl;

    peri(r);
    area(r);

    system("pause");

    return 0;
}

double PI = 3.14;

void peri (double r)
{
    cout << "peripheral length=" << 2 * PI * r << endl;

    return;
}

void area (double r)
{
    cout << "area=" << pi * r * r << endl;

    return;
}