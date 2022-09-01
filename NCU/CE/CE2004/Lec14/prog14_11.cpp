// This is the wrong example.

#include <iostream>
#include <cstdlib>

using namespace std;

class CWin
{
    private:
        char id, *title;

    public :
        CWin(char i = 'D', char *text = "Default window") : id(i)
        {
            cout << "The constructor has been called..." << endl;
            title = new char[strlen(text) + 1];
            strcpy(title, text);
        }
        
        CWin(const CWin &win)
        {
            cout << "The duplicated constructor has been called..." << endl;
            id = win.id;
            title = new char[strlen(win.title) + 1];
            strcpy(title, win.title);
        }

        ~CWin()
        {
            delete [] title;
        }

        void show()
        {
            cout << "Window " << id << ": " << title << endl;
        }
};

void display(CWin win)
{
    win.show();
}

int main(void)
{
    CWin *ptr1 = new CWin('A', "Main window");

    display(*ptr1);
    display(*ptr1);

    delete ptr1;

    system("pause");

    return 0;
}