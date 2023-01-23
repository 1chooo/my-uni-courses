#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int num = 5;
    int &rm = num;

    rm += 10;

    cout << "num=" << num << endl;
    cout << "rm=" << rm << endl;

    system("pause");

    return 0;
}