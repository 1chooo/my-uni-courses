#include <iostream>
#include <cstdlib>

namespace name1
{
    int var = 5;
}

using namespace name1;
using namespace std;

int main(void)
{
    cout << "var = " << var << endl;

    int var = 10;

    cout << "var in main(): " << var << endl;
    cout << "name1::var = " << name1::var << endl;

    system("pause");

    return 0;
}