#include <iostream>
#include <cstdlib>

using namespace std;

int main (int argc, char *argv[])
{
    int a = atoi(argv[1]);
    int b = atoi(argv[2]);

    cout << a << "+" << b << "=" << a + b << endl;

    system("pause");

    return 0;
}