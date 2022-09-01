#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int sum = 0;

    for (int i = 0; i <= 5; i++)
    {
        sum += 1;
        cout << "i=" << i << ", sum=" << sum << endl;
    }

    system("pause");

    return 0;
}