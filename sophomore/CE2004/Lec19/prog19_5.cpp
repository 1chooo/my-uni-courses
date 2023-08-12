#include <iostream>
#include <cstdlib>

using namespace std;

template <class T>

T add(T a, T b)
{
    T sum = a + b;

    return sum;
}

int main(void)
{
    cout << "add(3, 4) = " << add<int> (3, 4) << endl;
    cout << "add(3.2, 4.6) = " << add<double> (3.2, 4.6) << endl;

    system("pause");

    return 0;
}