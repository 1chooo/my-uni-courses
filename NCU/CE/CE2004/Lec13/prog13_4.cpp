#include <iostream>
#include <cstdlib>

class CWin
{
    private :
        char id;
        int width, height;

    public :
        CWin(char i, int w, int h)
        {
            id = i;
            width = w;
            height = h;

            cout << "The constructor CWin(char, int, int) have been called..." << endl;
        }

        CWin(int w, int h)
        {
            id = 'Z';
            width = w;
            height = h;

            cout << "The constructor CWin(int, int) have been called..." << endl;
        }

        CWin()
        {
            id = 'D';
            width = w;
            height = h;

            cout << "The default constructor have been called..." << endl;
        }

        void showMember(void)
        {
            cout << "Window " << id << ": ";
            cout << "width = " << width << ", height = " << height << endl;
        }
};

int main(void)
{
    CWin win1('A', 50, 40);
    CWin win2(80, 120);
    CWin win3;

    win1.showMember();
    win2.showMember();
    win3.showMember();

    system("pause");

    return 0;
}