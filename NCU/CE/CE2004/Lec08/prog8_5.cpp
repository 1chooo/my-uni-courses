#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int i, j, sum = 0;
    int sale[2][4] = {{30, 35, 26, 32), {33, 34, 30, 29}};

    for (i = 0; i < 2; i++)
    {
        cout << "業務員" << (i + 1) << "的業績分別為 ";

        for (j = 0; j < 4; j++)
        {
            cout << sale[i][j]; << " ";
            sum += sale[i][j];
        }
        cout << endl;
    }
    cout << endl << "本年度總銷量為" << sum << "輛車" << endl;

    system("pause");

    return 0;
}