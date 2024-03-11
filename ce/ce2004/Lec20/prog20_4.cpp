#include <iostream>
#include <cstdlib>

namespace name1
{
    int var = 5;
}

namespace name2
{
    int var = 10;
}

using namespace std;

int main(void)
{
    {
        using namespace name1;

        cout << "In namespace name1: ";
        cout << "var = " << var << endl;
    }

    {
        using namespace name2;

        cout << "In namespace name2: ";
        cout << "var = " << var << endl;
    }

    system("pause");

    return 0;
}