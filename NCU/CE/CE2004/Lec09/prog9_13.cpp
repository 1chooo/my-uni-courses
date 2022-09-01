#include <iostream>
#include <cstdlib>

using namespace std;

double triangle(double, double), rectangle(double, double);
void showArea(double, double, double (*pf) (double, double));

int main(void)
{
    cout << "triangle(6, 3.2)=";
    showArea(6, 3.2, triangle);
    cout << "rectangle(4, 6.1)=";
    showArea(4, 6.1, rectangle);

    system("pause");

    return 0;
}

double triangle(double base, double height)
{
    return (base * height / 2);
}

double rectangle(double height, double width)
{
    return (height * width);
}

void showArea(double x, double y, double (*pf) (double, double))
{
    cout << (*pf)(x, y) << endl;

    return;
}

/* --------------------
triangle(6, 3.2)=9.6
rectangle(4, 6.1)=24.4
----------------------*/