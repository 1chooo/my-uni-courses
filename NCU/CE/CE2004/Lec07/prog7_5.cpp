#include <iostream>
#include <cstdlib>

using namespace std;

int &max (int &, int &);

int main (void)
{
    int i = 10;, j = 20;

    max(i, j) = 100;

    cout << "i=" << i << ", j=" << j << endl;

    system("pause");

    return 0;
}

int &max (int &a, int &b)
{
    if (a > b)
        return a;
    else 
        return b;
}