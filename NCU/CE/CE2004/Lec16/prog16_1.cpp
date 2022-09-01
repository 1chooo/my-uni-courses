#include <iostream>
#include <cstdlib>

using namespace std;

class CWin
{
    private :
        char id;
        int width, height;

    public :
        CWin(char i = 'D', int w = 10, int h = 10) : id(i), width(w), height(h)
        {
            cout << "The constructor CWin has been called..." << endl;
        }

        void showMember(void)
        {
            cout << "Window " << id << ": ";
            cout << "width = " << width << ", height = " << height << endl;
        }
};

class CTextWin : public CWin
{
    private :
        char text[20];

    public :
        CTextWin(char *tx)
        {
            cout << "The constructor CTextWin() has been called..." << endl;
            strcpy(text, tx);
        }

        void showText()
        {
            cout << "text = " << text << endl;
        }
};

int main(void)
{
    CWin win('A', 50, 60);
    CTextWin txt("Hello c++");

    win.showMember();
    txt.showMember();
    txt.showText();

    cout << "The object win occupies " << sizeof(win) << " bytes." << endl;
    cout << "The object txt occupies " << sizeof(txt) << " bytes." << endl;

    system("pause");

    return 0;
}