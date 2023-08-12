#include <iostream>
#include <cstdlib>

using namespace std;

class CWin
{
    private :
        char id;
        int width, height;

    public :
        CWin(char i = 'D', int w = 100, int h = 100) : id(i), width(w), height(h)
        {
            cout << "The constructor has been called!" << endl;
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
    CWin myWin[3];

    win1.showMember();
    myWin[2].showMember();

    system("pause");

    return 0;
}