#include <iostream>
#include <cstdlib>

using namespace std;

void replace(int *, int, int);

int main(void)
{
    int a[5] = {1, 2, 3, 4, 5};
    int i, num = 100;

    cout << "Before replacing, the content of array: ";
    for (i = 0; i < 5; i++)
        cout << a[i] << " ";
    cout << endl;

    replace(a, 4, num);
    cout << "After replacing, the content of array: ";
    for (i = 0; i < 5; i++)
        cout << a[i] << " ";
    cout << endl;

    system("pause");

    return 0;
}


void replace(int *ptr, int n, int num)
{
    *(ptr + n - 1) = num;

    return;
}