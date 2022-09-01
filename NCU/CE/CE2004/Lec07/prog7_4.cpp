#include <iostream>
#include <cstdlib>

using namespace std;

void print (char, int &);

int main (void)
{
    int i, count = 0;

    for (i = 0; i < 3; i++)
        print('*', count);
    cout << endl;

    for (i = 0; i < 5; i++)
        print('$', count);
    cout << endl;

    cout << "print() function is called " << count << " times."
    cout << endl;

    system("pause");

    return 0;
}

void print (char ch, int & cnt)
{
    cout << ch;
    cnt++;

    return;
}