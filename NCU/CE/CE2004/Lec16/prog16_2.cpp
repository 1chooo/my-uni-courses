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
            cout << "The constructor CWin() has been called..." << endl;
        }

        CWin(int w, int h) : width(w), height(h)
        {
            cout << "The constructor CWin(int w, inth) has been called..." << endl;
            id = 'K';
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
        CTextWin(int w, int h) : CWin(w, h)
        {
            cout << "The constructor CTextWin(int w, int h) has been called..." << endl;
            strcpy(text, "Have a good night");
        }

        CTextWin(char *tx)
        {
            cout << "The constructor CTextwin(char *tx) has been called..." << endl;
            strcpy(text, tx);
        }

        void showText()
        {
            cout << "text = " << text << endl;
        }
};

int main(void)
{
    CTextWin tx1("Hello C++");
    CTextWin tx2(60, 70);

    tx1.showMember();
    tx1.showText();

    tx2.showMember();
    tx2.showText();

    system("pause");

    return 0;
}