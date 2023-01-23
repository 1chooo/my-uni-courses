#include <iostream>
#include <cstdlib>

using namespace std;

void add10 (int *);

int main (void)
{
    int a = 5;

    cout << "Before calling add10(), a=" << a << endl;

    add10(&a);
    cout << "After calling add10(), a=" << a << endl;

    system("pause");

    return 0;
}

void add10 (int *p1)
{
    *p1 = *p1 + 10;

    return;
}