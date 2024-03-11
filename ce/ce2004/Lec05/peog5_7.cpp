#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    for (int i = 1; i <= 3; i++)
    {
        for (int j = 1; j <= 3; j++)
            cout << i << "*" << j << "=" << i * j << "\t";
            
        cout << endl;
    }

    system("pause");

    return 0;
}