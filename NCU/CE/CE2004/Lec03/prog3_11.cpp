#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    bool status = false;
    cout << "status=" << status << endl;

    status = 1;
    cout << "status=" << status << endl;

    system("pause");

    return 0;
}