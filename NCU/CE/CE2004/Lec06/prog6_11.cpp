#include <iostream>
#include <cstdlib>
#include <ctime>
#include <iomanip>

using namespace std;

int main (void)
{
    time t start, end;
    register int i, j;

    start = time(NULL);

    for (i = 1; i <= 50; i++)
    {
        for (j = 1; j <= 50; j++)
        {
            cout << setw(2) << i << "*" << setw(2) << j;
            cout << "=" << setw(4) << i * j << "\t";
        }
        cout << endl;
    }

    end = time(NULL);

    cout << "It spends " << difftime(end, start) << "seconds" << endl;

    system("pause");

    return 0;
}