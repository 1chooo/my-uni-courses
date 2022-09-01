#include <iostream>
#include <cstdlib>

using namespace std;

int main(void)
{
    int num[3][4] = {{12, 23, 42, 18},
                     {43, 22, 16, 14},
                     {31, 13, 19, 28}};
    int n, m;

    for (m = 0; m < 3; m++)
        for (n = 0; n < 4; n++)
        {
            cout << "num[" << m << "][" << n << "]=" << *(*(num + m) + n);
            cout << ", the address is: " << *(num + m) + n << endl;
        }
    
    cout << "**num=" << **num << endl;  // point to num[0][0]

    system("pause");

    return 0;
}