#include <iostream>
#include <cstdlib>

using namespace std;

#define SIZE 5

void show (int []);
double average (int []);

int main (void)
{
    int score[SIZE] = {89, 54, 73, 95, 71};

    cout << "Students' score are ";
    show(score);
    cout << "Average score is " << average(score) << endl;

    system("pause");

    return 0;
}

void show (int a[])
{
    for (int i = 0; i < SIZE; i++)
        cout << a[i] << " ";
    cout << endl;

    return;
}

double average (int a[])
{
    double sum = 0;

    for (int i = 0; i < SIZE; i++)
        sum += a[i];
    
    return (sum / SIZE);
}