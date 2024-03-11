#include <iostream>
#include <cstdlib>

using namespace std;

void swap (int *, int *);

int main (void)
{
    int a = 5, b = 20;

    cout << "Before swappping, a=" << a << ", b=" << b << endl;

    swap(&a, &b);
    cout << "After swapping, a=" << a << ", b=" << b << endl;

    system("pause");

    return 0;
}

void swap (int *x, int *y)
{
    int tmp = *x;
    
    *x = *y;
    *y = tmp;

    return;
}