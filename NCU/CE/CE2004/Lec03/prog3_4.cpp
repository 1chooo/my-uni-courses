// Type of the char

#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    char chrA;

    /*
    both are represented character a.

    chrA = 'a';
    chrA = 97;
    chrA = 0x61;
    chrA = '7';
    */

   /*
   this represent the last value: f.
   chrA = 'abcdef';
   */

    char ch = 'h';
    int i = ch; 

    cout << "ch=" << ch << endl;
    cout << "The ASCII code is " << i << endl;

    system("pause");

    return 0;
}