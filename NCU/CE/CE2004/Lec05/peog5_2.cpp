#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int a = 5, b = 12, min;
    
    min = (a < b) ? a : b;  // conditional operator bool ? true : false

    cout << "a=" << a << ", b=" << b << endl;
    cout << min << "is smaller number." << endl;

    system("pause");

    return 0;
}