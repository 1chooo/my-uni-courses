#include <iostream>
#include <cstdlib>

using namespace std;

class CWin
{
    private :
        char id;
        int width, height;

    public :
        CWin(char i, int w, int h) : id(i), width(w), height(h)
        {
            cout << "The constructor has been called..." << endl;
        }

        ~CWin()
        {
            cout << "The deconstructor has been called..., Win ";
            cout << this-> id << " has been destroyed..." << endl;

            system("pause");
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
    CWin win2('B', 40, 50);
    CWin win3('C', 60, 70);
    CWin win4('D', 90, 40);

    win1.showMember();
    win2.showMember();

    system("pause");
    return 0;
}