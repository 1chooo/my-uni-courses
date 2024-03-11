#include <iostream>

using namespace std;

int main ()
{
    int firstColumn, secondColumn;
    int firstRow, secondRow;
    int A[10][10], B[10][10];
    int mul;
    int i, j, k;

    cout << "Matrix A size = ";
    cin >> firstColumn >> firstRow;
    cout << "Matrix B size = ";
    cin >> secondColumn >> secondRow;

    if (firstRow != secondColumn) {
        cout << "Can't be multiplied";
    }
    else {
        cout << "Matrix A" << endl;
        for (int i = 0; i < firstColumn; i++) {
            for (int j = 0; j < firstRow; j++) {
                cin >> A[i][j];
            }
        }

        cout << "Matrix B" << endl;
        for (int i = 0; i < secondColumn; i++) {
            for (int j = 0; j < secondRow; j++) {
                cin >> B[i][j];
            }
        }

        cout << "Multiplication" << endl;
        for (int i = 0; i < firstColumn; i++) {
            for (int j = 0; j < secondRow; j++) {
                mul = 0;
                for (int k = 0; k < secondColumn; k++){
                    mul += A[i][k] * B[k][j];
                }
                cout << mul << " ";
            }
            cout << endl;
        }
    }
    cout << endl;

    return 0;
}
