#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int x, y;

    cout << "Input first integer";
    cin >> x;
    cout << "Input second integer:";
    cin >> y;

    cout << x << "+" << y << "=" << x + y << endl;
    
    system("pause");

    return 0;
}