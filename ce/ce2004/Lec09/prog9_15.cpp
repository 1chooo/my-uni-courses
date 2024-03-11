#include <iostream>
#include <cstdlib>

using namespace std;

int main(void)
{
    int a[3] = {5, 7, 9};

    cout << "a[0]=" << a[0] << ", *(a+0)=" << *(a + 0) << endl;
    cout << "a[1]=" << a[1] << ", *(a+1)=" << *(a + 1) << endl;
    cout << "a[2]=" << a[2] << ", *(a+2)=" << *(a + 2) << endl;

    system("pause");

    return 0;
}