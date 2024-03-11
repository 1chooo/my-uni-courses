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

        CWin compare(CWin win)
        {
            if (this-> area() >= win.area())
                return *this;
            else 
                return win;
        }

        int area(void)
        {
            return width * height;
        }

        char getId(void)
        {
            return id;
        }
};

int main(void)
{
    CWin win1('A', 70, 80);
    CWin win2('B', 60, 90);

    cout << "Window " << (win1.compare(win2)).getId();
    cout << " is larger" << endl;

    system("pause");

    return 0;
}