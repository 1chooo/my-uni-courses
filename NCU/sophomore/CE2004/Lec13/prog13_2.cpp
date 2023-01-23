#include <iostream>
#include <cstdlib>

using namespace std;

class CWin
{
    private :
        char id;
        int width, height;

    public :
        CWin(char, int, int);

        void showMember(void)
        {
            cout << "Window " << id << ": ";
            cout << "width = " << width << ", height = " << height << endl;
        }
};

CWin::CWin(char i, int w, int h)
{
    id = i;
    width = w;
    height = h;

    cout << "The constructor CWin have been called..." << endl;
}

int main(void)
{
    CWin win1('A', 50, 40);
    CWin win2('B', 60, 70);

    win1.showMember();
    win2.showMember();

    system("pause");

    return 0;
}