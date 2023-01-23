#include <iostream>
#include <cstdlib>

using namespace std;

int main(void)
{
    char name[20];
    char *ptr = "How are you?";

    cout << "What's your name? ";
    cin.getline(name, 20);
    cout << "Hi, " << name << ", " << ptr << endl;
    
    /*
    cout << (++name) << endl;
    cout << (++ptr) << endl; 

    the sixteenth line will occur error because 
    cannot increment value of type 'char'.
    */

    system("pause");

    return 0;
}