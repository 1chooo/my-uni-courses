#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int A[] = {48, 75, 30, 17, 62};
    int i, main = A[0], max = A[0];
    int length = sizeof(A) / sizeof(int);

    cout << "elements in array A are ";

    for (i = 0; i < length; i++)
    {
        cout << A[i] << " ";

        if (A[i] > max)
            max = A[i];
        if (A[i] < min)
            min = A[i];
    }

    cout << endl << "Maximum is " << max;
    cout << endl << "Minimum is " << min << endl;

    system("pause");

    return 0;
}