#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    char name[15];
    int i;

    for (i = 0; i < 2; i++)
    {
        cout << "What's your name? ";
        cin.getline(name, 15);      // use getline may correct the error.
        cout << "Hi, " << name << ", how are you?" << endl << endl;
    }

    system("pause");

    return 0;
}