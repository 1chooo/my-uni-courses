// This is the wrong example to called super class

#include <iostream>
#include <cstdlib>

using namespace std;

class CWin
{
    private :
        char id;
        int width, height;

    public :
        CWin(int w, int h) : width(w), height(h)
        {
            cout << "The constructor CWin(int w, int h) has been called..." << endl;
            id = 'K';
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
};

int main(void)
{
    CTextWin tx1("Hello C++");

    system("pause");

    return 0;
}