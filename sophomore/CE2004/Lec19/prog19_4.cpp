#include <iostream>
#include <cstdlib>

using namespace std;

int add(int a, int b)
{
    return a + b;
}

double add(double a, double b)
{
    return a + b;
}

int main(void)
{
    cout << "add(3, 4) = " << add(3, 4) << endl;
    cout << "add(3.2, 4.6) = " << add(3.2, 4.6) << endl;

    system("pause");

    return 0;
}