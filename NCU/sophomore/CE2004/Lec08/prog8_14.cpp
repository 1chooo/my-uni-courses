#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int age;
    char name[20];

    cout << "How old are you? ";
    cin >> age;

    /* 
    It will occur the error. 
    Therefore we have to receive the rest of "\n"
    We add cin.get()
    */ 

    cin.get();

    cout << "What's your name? ";
    cin.getline(name, 20);      
    cout << name << " is " << age << "-years-old!" << endl;

    system("pause");

    return 0;
}