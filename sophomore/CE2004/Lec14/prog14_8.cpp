// It's the wrong example.

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
            cout << "The constructor has been called..." << endl;
            title = new char[strlen(text) + 1];
            strcpy(title, text);
        }

        CWin(const CWin &win)
        {
            cout << "The duplicated constructor has been called..." << endl;
            id = win.id;
            title = win.title;
        }

        ~CWin()
        {
            delete [] title;
        }

        void show(void)
        {
            cout << "Window " << id << ": " << title << endl;
        }
};

int main(void)
{
    CWin *ptr1 = new CWin('A', "Main window");
    CWin *ptr2 = new CWin(*ptr1);

    ptr1 -> show();
    ptr2 -> show();

    delete ptr1;
    cout << "After deleting the object that ptr1 points..." << endl;
    ptr2 -> show();

    delete ptr2;

    system("pause");

    return 0;
}