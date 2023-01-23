#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int i;
    char students[3][15];

    for (i = 0; i < 3; i++)
    {
        cout << "Input student" << i << "'s name:";
        cin.getline(students[i], 15);
    }

    cout << "***OUTPUT***" << endl;

    for (i = 0; i < 3; i++)
        cout << "students[" << i << "]=" << students[i] << endl;
    
    system("pause");

    return 0;
}

/*
Input student0's name:Marry Wang
Input student1's name:Queens
Input student2's name:Jerry Ho
***OUTPUT***
students[0]=Marry Wang
students[1]=Queens
students[2]=Jerry Ho
sh: pause: command not found
*/