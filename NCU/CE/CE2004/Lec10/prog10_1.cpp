#include <iostream>
#include <cstdlib>

using namespace std;

int main(void)
{
    int n = 20, *p, **pp;
    p = &n;
    pp = &p;

    cout << "n=" << n << ", &n=" << &n << ", *p=";
    cout << *p << ", p=" << p << ", &p=" << &p << endl;
    cout << "**pp=" << **pp << ", *pp=" << *pp;
    cout << ", pp=" << pp << ", &pp=" << &pp << endl;
    
    system("pause");
    
    return 0;
}