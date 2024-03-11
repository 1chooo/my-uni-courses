#include <iostream>
#include <cstdlib>

using namespace std;

class CWin
{
    private :
        char id, title[20];

    public :
        CWin(char i = 'D', char *text = "Default window") : id(i)
        {
            strcpy(title, text);
        }

        ~CWin()
        {
            cout << "The deconstructor has been called..., Win ";
            cout << this-> id << " has been destroyed..." << endl;

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
    CWin win2('B');

    win1.show();
    win2.show();

    cout << "sizeof(win1) = " << sizeof(win1) << endl;
    cout << "sizeof(win2) = " << sizeof(win2) << endl;

    system("pause");

    return 0;
}