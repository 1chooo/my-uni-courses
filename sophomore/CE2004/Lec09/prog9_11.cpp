#include <iostream>
#include <cstdlib>

using namespace std;

int *max (int *, int *);

int main (void)
{
    int a = 12, b = 17, *ptr;

    ptr = max(&a, &b);
    cout << "max=" << *ptr << endl;

    system("pause");

    return 0;
}

int *max (int *p1, int *p2)
{
    if (*p1 > *p2)
        return p1;
    else
        return p2;
}