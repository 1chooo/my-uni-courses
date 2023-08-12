#include <iostream>
#include <cstdlib>

using namespace std;

void address (int *);

int main (void)
{
    int a = 12;
    int *ptr = &a;

    address(&a);
    address(ptr);

    system("pause");

    return 0;
}

void address (int *p1)
{
    cout << "In the address " << p1 ;
    cout << ", the content of the storing variable is ";
    cout << *p1 << endl;
}