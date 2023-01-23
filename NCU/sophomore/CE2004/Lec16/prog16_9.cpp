/*
 This is the wrong example that
 there's no duplicated constructor
 in sub class.
 */

#include <iostream>
#include <cstdlib>

using namespace std;

class CWin
{
    protected :
        char id;

    public :
        CWin(char i = 'D') : id(i)
        {
            cout << "The constructor CWin() has been called..." << endl;
        }

        CWin(const CWin &win)
        {
            cout << "The duplicated constructor CWin() has been called..." << endl;
            id = win.id;
        }

        ~CWin()
        {
            cout << "The deconstructor ~CWin() has been called..." << endl;

            system("pause");
        }
};

class CTextWin : public CWin
{
    private :
        char *text;

    public :
        CTextWin(char i, char *tx) : CWin(i)
        {
            cout << "The constructor CTextWin() has been called..." << endl;
            text = new char[strlen(tx) + 1];
            strcpy(text, tx);
        }

        ~CTextWin()
        {
            delete [] text;
            cout << "The deconstructor CTextWin() has been called..." << endl;

            system("pause");
        }

        void showMember()
        {
            cout << "Window " << id << ": ";
            cout << "text = " << text << endl;
        }

        void setMember(char i, char *tx)
        {
            id = i;
            delete [] text;
            text = new char[strlen(tx) + 1];
            strcpy(text, tx);
        }
};

int main(void)
{
    CTextWin tx1('A', "Hello C++");
    CTextWin tx2(tx1);

    tx1.showMember();
    tx2.showMember();

    cout << "After changing member of the object tx1... " << endl;
    tx1.setMember('B', "Welcome C++");

    tx1.showMember();
    tx2.showMember();

    system("pause");

    return 0;
}