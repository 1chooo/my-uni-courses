#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

int main (void)
{
    char str1[] = "";
    string str2;

    cout << "str1=" << str1 << endl;
    cout << "sizeof(str1)=" << sizeof(str1) << endl;
    cout << "str2=" << str2 << endl;
    cout << "length=" << str2.length() << endl;

    system("pause");

    return 0;
}