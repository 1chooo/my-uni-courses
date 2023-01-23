#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    char beep = '\a';
    int i = beep;

    cout << "beep=" << beep;    // 跳脫字元
    cout << i << endl;

    system("pause");

    return 0;
}