// This is worong example

#include <iostream>
#include <cstdlib>

using namespace std;

class CWin
{
    private :
        char id, *title;

    public :
        CWin(char i = 'D', char *text = "Default window") : id(i)
        {
            title = new char[strlen(text) + 1];
            strcpy(title, text);
        }

        ~CWin()
        {
            cout << "The deconstructor has been called..., Win ";
            cout << this-> id << " has been destroyed..." << endl;

            delete [] title;

            system("pause");
        }

        void show(void)
        {
            cout << "Window " << id << ": " << title << endl;
        }
};

int main(void)
{
    CWin win1('A', "Main window");
    CWin *ptr;

    ptr = new CWin('B');

    win1.show();
    ptr->show();

    system("pause");

    return 0;
}