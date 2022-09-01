#include <iostream>
#include <cstdlib>

using namespace std;

#define POWER(X) X * X * X

int main (void)
{
    int i;

    cout << "Input an integer:";
    cin >> i;

    // This version will occur error.
    cout << i + 1 << "*" << i + 1 << "*" << i + 1 << "=" << POWER(i + 1) << endl;

    system("pause");

    return 0; 
}