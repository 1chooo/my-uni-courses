#include <iostream>
#include <cstdlib>

using namespace std;

void func (void);

int main (void)
{
    func();
    func();
    func();

    system("pause");

    return 0;
}

void func (void)
{
    static int a = 30;
    
    cout << "In func(), a=" << a << endl;

    a += 20;

    return;
}