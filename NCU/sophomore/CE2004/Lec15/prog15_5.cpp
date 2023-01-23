// To correct the error of prog15_4.cpp

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
            title = new char[50];
            strcpy(title, text);
        }

        void setData(char i, char *text)
        {
            id = i;
            strcpy(title, text);
        }

        void operator = (const CWin &win)
        {
            id = win.id;
            strcpy(this -> title, win.title);
        }

        void show(void)
        {
            cout << "Window " << id << ": " << title << endl;
        }

        ~CWin()
        {
            delete [] title;
        }

        CWin(const CWin &win)
        {
            id = win.id;
            strcpy(title, win.title);
        }
};

int main(void)
{
    CWin win1('A', "Main window");
    CWin win2;

    win1.show();
    win2.show();

    win1 = win2;
    cout << endl << "After seeting win1 = win2..." << endl;
    win1.show();
    win2.show();

    win1.setData('B', "Hello window");
    cout << endl << "After changing the data of win1's member..." << endl;
    win1.show();
    win2.show();

    system("pause");

    return 0;
}