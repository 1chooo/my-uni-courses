#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int num = 42;
    if (num % 3 == 0 && num % 7 == 0)
        cout << num << "can be divided exactly by 3 and 7." << endl;
    else
        cout << num << "can not be divided exactly by 3 and 7." << endl;

    system("pause");

    return 0;
}