#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int a, b;

    cout << "Please input the value of integer a: ";
    cin >> a;
    cout << "Please input the value of integer b: ";
    cin >> b;

    cout << "The result of a&b is: " << (a & b) << endl;
    cout << "The result of a|b is: " << (a | b) << endl;
    cout << "The result of a^b is: " << (a ^ b) << endl;
    cout << "The result of a>>2 is: " << (a >> 2) << endl;  // 運算元全部往右移2, 相當於除2
    cout << "The result of a<<2 is: " << (a << 2) << endl;  // 運算元全部往左移2, 相當於乘2

    system("pause");

    return 0;
}

/*
Please input the value of integer a: 45
Please input the value of integer b: 7
The result of a&b is: 5
The result of a|b is: 47
The result of a^b is: 42
The result of a>>2 is: 11
The result of a<<2 is: 180
*/