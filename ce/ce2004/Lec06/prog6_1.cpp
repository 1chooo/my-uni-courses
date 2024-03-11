#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    star();
    cout << "6*6=" << 6 * 6 << endl;
    star();

    system("pause");

    return 0;
}

void star(void)
{
    int j;
    for (j = 1; j <= 8; j++)
        cout << "*";
    cout << endl;
    return;
}