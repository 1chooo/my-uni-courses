// This is to correct prog16_3.cpp

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

        CWin()
        {
            cout << "The constructor CWin() which has no argument has been called..." << endl;
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