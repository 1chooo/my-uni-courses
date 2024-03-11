#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int *ptri;
    char *ptrc;

    cout << "sizeof(ptri)=" << sizeof(ptri) << endl;
    cout << "sizeof(ptrc)=" << sizeof(ptrc) << endl;
    cout << "sizeof(*ptri)=" << sizeof(*ptri) << endl;
    cout << "sizeof(*ptrc)=" << sizeof(*ptrc) << endl;

    system("pause");

    return 0;
}