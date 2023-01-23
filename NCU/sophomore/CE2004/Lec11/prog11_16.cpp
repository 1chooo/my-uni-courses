#include <iostream>
#include <cstdlib>

using namespace std;

enum sports
{
    tennis,
    swimming,
    baseball,
    ski
} favorite = ski;

int main(void)
{
    cout << "favorite=";
    switch (favorite)
    {
        case 0: cout << "tennis" << endl;
            break;
        case 1: cout << "swimming" << endl;
            break;
        case 2: cout << "baseball" << endl;
            break;
        case 3: cout << "ski" << endl;
    }

    system("pause");

    return 0;
}