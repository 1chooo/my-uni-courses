#include <iostream>
#include <set>
#include <vector>

using namespace std;

int main ()
{
    while (1) {
        int size;
        int i, j;
        int count = 0;
        int matrix[100][100];

        cout << "Input Size: ";
        cin >> size;
        if (size == -1) {
            cout << endl;
            break;
        }

        for (i = 0; i < size; i++) {
            for (j = 0; j < size; j++) {
                cin >> matrix[i][j];
            }
        }

        for (i = 0; i < size; i++) {
            for (j = 0; j < size; j++) {
                if (matrix[i][j] == matrix[(size - 1) - i][(size - 1) - j]) {
                    count ++;
                }
            }
        }

        if (count == size * size) {
            cout << "Symmetric!" << endl;
        }
        else {
            cout << "Non-Symetric!" << endl;
        }
    }

    return 0;
}