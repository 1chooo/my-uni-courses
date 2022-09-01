#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int a = 8, b = 5, c = 9, d = 2;

    cout << "a=8, b=5, c=9, d=2\n";
    cout << "The result of a>b & c>d is: " << (a > b & c > d) << "\n";
    cout << "The result of a<b | c<d is: " << (a < b | c < d) << "\n";
    cout << "The result of a>b ^ c>d is: " << (a > b ^ c > d) << "\n";
    cout << "The result of !(a<b) is:    " << !(a < b) << "\n";

    system("pause");

    return 0;
}