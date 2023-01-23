#include <iostream>
#include <cstdlib>
#include "./area.h"

using namespace std;

int main (void)
{
    float base, height;

    cout << "Input the base of triangle:";
    cin >> base;
    cout << "Input the height of triangle:";
    cin >> height;

    cout << "The area of triangle is " << TRIANGLE(base, height) << endl;

    system("pause");

    return 0;
}