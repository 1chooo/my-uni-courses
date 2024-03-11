#include <iostream>
#include <cstdlib>

using namespace std;

#define POWER i * i * i

int main (void)
{
    int i;

    cout << "Input an integer:";
    cin >> i;

    cout << i << "*" << i << "*" << i << "=" << POWER << endl;

    system("pause");

    return 0; 
}