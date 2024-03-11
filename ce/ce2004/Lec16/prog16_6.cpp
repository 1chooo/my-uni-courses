/*
 This is to correct the wrong in prog16_5.cpp
 */

#include <iostream>
#include <cstdlib>

using namespace std;

class CWin
{
    private :
        char id;

    public :
        CWin(char i) : id(i)
        {}

        char getId()
        {
            return id;
        }
};

class CTextWin : public CWin
{
    private :
        char text[20];

    public :
        CTextWin(char i, char *tx) : CWin(i)
        {
            strcpy(text, tx);
        }

        void show()
        {
            cout << "Window " << getId() << ": ";
            cout << "text = " << text << endl;
        }
};

int main(void)
{
    CTextWin txt('A', "Hello C++");

    txt.show();

    system("pause");

    return 0;
}