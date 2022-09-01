#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int i = 369;
    char ch = i;

    // it will only take the last 8 bits.
    cout << "ch=" << ch << endl;

    system("pause");

    return 0;
}