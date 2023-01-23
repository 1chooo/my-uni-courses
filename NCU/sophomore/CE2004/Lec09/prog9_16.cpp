#include <iostream>
#include <cstdlib>

using namespace std;

int main(void)
{
    int a[3] = {5, 7, 9};
    int i, sum = 0;

    for (i = 0; i < 3; i++)
        sum += *(a + i);
    
    cout << "sum=" << sum << endl;

    system("pause");

    return 0;
}