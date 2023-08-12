// inline function

#include <iostream>
#include <cstdlib>

using namespace std;

inline void star (void)
{
    cout << "*************" << endl;
}

int main (void)
{
    star();
    cout << "Hello, C++" << endl;
    star();

    system("pause");

    return 0;
}