#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    unsigned int i = 0;
    unsigned short int j = 0;
    char ch = ' ';
    float f = 0.0f;
    double d = 0.0;

    cout << "sizeof(int)=" << sizeof(int) << endl;
    cout << "sizeof(long int)=" << sizeof(long int) << endl;
    cout << "sizeof(unsigned int)=" << sizeof(short int) << endl;
    cout << "sizeof(unsigned short int)=" << sizeof(unsigned short int) << endl;
    cout << "sizeof(char)=" << sizeof(char) << endl;
    cout << "sizeof(float)=" << sizeof(float) << endl;
    cout << "sizeof(double)=" << sizeof(double) << endl;
    cout << "sizeof(bool)=" << sizeof(bool) << endl;

    system("pause");

    return 0;
}