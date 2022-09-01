#include <iostream>
#include <cstdlib>

using namespace std;

int main(void)
{
    int num[3][4];

    cout << "num=" << num << endl;
    cout << "&num=" << &num << endl;
    cout << "*num=" << *num << endl;

    cout << "num[0]=" << num[0] << endl; 
    cout << "num[1]=" << num[1] << endl; 
    cout << "num[2]=" << num[2] << endl;

    cout << "&num[0]=" << &num[0] << endl; 
    cout << "&num[1]=" << &num[1] << endl; 
    cout << "&num[2]=" << &num[2] << endl; 

    system("pause");

    return 0;
}