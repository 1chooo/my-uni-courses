#include <iostream>
#include <cstdlib>

using namespace std;

int main(void)
{
    int i, a[5] = {32, 16, 35, 65, 52};

    cout << "a=" << a << endl;
    cout << "&a=" << &a << endl;

    for (i = 0; i < 5; i++)
        cout << "&a[" << i << "]=" << &a[i] << endl;

    system("pause");

    return 0;
}