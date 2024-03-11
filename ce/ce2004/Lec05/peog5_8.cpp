#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int i;

    for (i = 1; i <= 10; i++)
    {
        if (i % 4 == 0)
            break;
            
        cout << "i=" << i << endl;
    }

    cout << "when loop interrupted, i=" << i << endl;

    system("pause");

    return 0;
}