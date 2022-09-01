#include <iostream>
#include <cstdlib>

using namespace std;

void sum (int), fact (int);

int main (void)
{
    int a = 5;
    fact(a);
    sum(a);

    system("pause");

    return 0;
}

void fact (int a)
{
    int i, total = 1;

    for (i = 1; i <= a; i++)
        total *= i;
    
    cout << "1*2*...*" << a << "=" << total << endl;

    return;
}

void sum (int a)
{
    int i, sum = 0;
    for (i = 1; i <= a; i++)
        sum += i;

    cout << "1+2+...+" << a << "=" << sum << endl;

    return;
}