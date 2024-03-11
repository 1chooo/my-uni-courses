#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    char ch = 'X';      // 1 byte
    short s = -5;       // 2 bytes
    int i = 6;          // 4 bytes
    float f = 9.7f;     // 4 bytes
    double d = 1.76;    // 8 bytes

    /*
    (s*ch) s still "short type", but ch convert to "short type".
    (d/f) d still "double type", but f convert to "double type".
    (i+f) f still "float type", but i convertr to "float type".

    then the final, above of all the result will be converted
    to the "double type".
    */

    cout << "(s*ch)-(d/f)*(i+f)=";
    cout << (s * ch) - (d / f) * (i + f) << endl;

    system("pause");

    return 0;
}