#include <iostream>
#include <cstdlib>

using namespace std;

#define LENGTH 2
#define WIDTH 5

void show (int [LENGTH][WIDTH]);

int main (void)
{
    int A [LENGTH][WIDTH] = {{81, 52, 13, 96, 27},
                             {24, 23, 10, 32, 16}};

    show(A);

    system("pause");

    return 0;
}

void show (int a[LENGTH][WIDTH])
{
    for (int i = 0; i < LENGTH; i++)
    {
        for (int j = 0; j < WIDTH; j++)
            cout << a[i][j] << " ";
        cout << endl;
    }

    return;
}