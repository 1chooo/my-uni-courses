#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int i, sum = 0;

    for (int i = 0; i <= 15; i++)
        sum += 1;

    cout << "1+2+...+15" << sum << endl;

    system("pause");

    return 0;
}