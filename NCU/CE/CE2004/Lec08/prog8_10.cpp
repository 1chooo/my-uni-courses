#include <iostream>
#include <cstdlib>
#include <iomanip>

using namespace std;

void func (int []);

int main (void)
{
    int i, a[4] = {20, 8, 13, 6};

    cout << "In main()," << endl;

    for (i = 0; i < 4; i++)
    {
        cout << "a[" << i << "]=" << setw(2) << a[i];
        cout << ", address=" << &a[i] << endl;
    }

    func(a);

    system("pause");

    return 0;
}

void func (int b[])
{
    int i;

    cout << "In func()," << endl;

    for (i = 0; i < 4; i++)
    {
        cout << "b[" << i << "]=" << setw(2) << b[i];
        cout << ", address=" << &b[i] << endl;
    }

    return;
}