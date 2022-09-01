// This contain semantic error; therefore, it still can run.

#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int num1 = 35;
    int num2 = 28;

    cout << "I have " << num1 << " books." << endl;
    cout << "You have " << num2 << " books." << endl;
    cout << "We have " << (num1 - num2) << " books." << endl;

    system("pause");

    return 0;
}