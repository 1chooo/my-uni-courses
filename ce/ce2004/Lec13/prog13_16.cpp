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
        {}

        void compare(CWin &win)
        {
            if (this-> area() > win.area())
                cout << "Window " << this-> id << " is larger" << endl;
            else 
                cout << "Window " << win.id << " is larger" << endl;
        }

        int area(void)
        {
            return width * height;
        }
};

int main(void)
{
    CWin win1('A', 70, 80);
    CWin win2('B', 60, 90);

    win1.compare(win2);

    system("pause");

    return 0;
}