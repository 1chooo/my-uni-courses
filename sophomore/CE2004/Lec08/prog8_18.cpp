#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

int main (void)
{
    string str1 = "Hank ";
    string str2 = "Wang";
    string str3 = ", 2022/07/09";

    cout << "str1=" << str1 << ", str2=" << str2;
    cout << ", str3=" << str3 << endl;

    cout << "Conduct str1.append(str2) " << endl;
    str1.append(str2);
    cout << "str1=" << str1 << endl;

    cout << "Conduct str1.append(str3, 0, 6)" << endl;
    str1.append(str3, 0, 6);
    cout << "str1=" << str1 << endl;

    cout << "After taking out the fifth character in str1 --> ";
    cout << str1.substr(5) << endl;
    cout << "Length of str1=" << str1.length() << endl;

    system("pause");

    return 0;
}