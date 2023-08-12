#include <iostream>
#include <cstdlib>

using namespace std;

int main(void)
{
    typedef float temper;
    temper f, c;

    cout << "Input Celsius degree: ";
    cin >> c;
    f = (float) (9.0 / 5.0) * c + 32;
    cout << c << " Celcius is equal to ";
    cout << f << " Fahrenheit degrees." << endl;

    system("pause");

    return 0;
}