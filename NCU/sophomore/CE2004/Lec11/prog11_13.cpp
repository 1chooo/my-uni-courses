#include <iostream>
#include <cstdlib>

using namespace std;

enum month
{
    January,
    February,
    March = 4,
    April,
    May,
    June
} six;

int main(void)
{
    cout << "sizeof(six)=" << sizeof(six) << endl;
    cout << "January=" << January << endl;
    cout << "February=" << February << endl;
    cout << "March=" << March << endl;
    cout << "April=" << April << endl;
    cout << "May=" << May << endl;
    cout << "June=" << June << endl;

    system("pause");

    return 0;
}