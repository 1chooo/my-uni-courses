#include <iostream>
#include <cstdlib>

using namespace std;

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
    /*
    It might complie error.
    CWin win3;
    */

    win1.showMember();
    win2.showMember();
    
    system("pause");

    return 0;
}