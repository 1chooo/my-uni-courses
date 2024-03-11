#include <iostream>
#include <cstdlib>

using namespace std;

class CWin
{
    protected :
        char id;

    public :
        CWin(char i) : id(i)
        {}

        void showMember(void)
        {
            cout << "The function showMember() in super class has been called..." << endl;
            cout << "Window " << id << endl;
        }
};

class CTextWin : public CWin
{
    private : 
        char text[20];

    public :
        CTextWin(char i, char *tx) : CWin('i')
        {
            strcpy(text, tx);
        }

        void showMember()
        {
            cout << "The function showMember() in sub class has been called..." << endl;
            cout << "Window " << id << ": ";
            cout << "text = " << text << endl;
        }
};

int main(void)
{
    CTextWin txt('A', "Hello C++");

    txt.showMember();

    system("pause");

    return 0;
}