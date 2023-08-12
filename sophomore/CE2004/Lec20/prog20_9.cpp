#include <iostream>
#include <cstdlib>

#define STR "Hello C++"

using namespace std;

int main(void)
{
    #ifdef STR
        cout << STR << endl;
    #else
        cout << "STR not defined" << endl;
    #endif

    system("pause");

    return 0;
}