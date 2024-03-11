#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    char ch = '\\';     // 跳脫序列
    cout << ch << "Live and learn!" << ch << endl;

    system("pause");

    return 0;
}