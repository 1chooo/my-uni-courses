#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int a = 10;

    cout << "a=" << a << endl;
    cout << "a++*2=" << (++a * 2) << endl;  // add 1 before multiply 2 
    cout << "a=" << a << endl;

    system("pause");

    return 0;
}