#include <iostream>
#include <cstdlib>

using namespace std;

void print (void);
void print (int);
void print (char, int);

int main (void)
{
    cout << "calling print(), ";
    print();

    cout << "calling print(8), ";
    print(8);

    cout << "calling print('+', 3), ";
    print('+', 3);

    system("pause");

    return 0;
}

void print (void)
{
    print(5);
    
    return;
}

void print (int a)
{
    int i;

    for (i = 0; i < a; i++)
        cout << "*";
    cout << endl;

    return;
}

void print (char ch, int a)
{
    int i;

    for (i = 0; i < a; i++)
        cout << ch;
    cout << endl;

    return;
}