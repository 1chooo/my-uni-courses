#include <iostream>
#include <cstdlib>

using namespace std;

class CShape
{
    public :
        virtual int area() = 0;

        void showArea()
        {
            cout << "area = " << area() << endl;
        }
};

class CWin : public CShape
{
    protected :
        int width, height;

    public :
        CWin(int w = 10, int h = 10)
        {
            width = w;
            height = h;
        }

        virtual int area()
        {
            return width * height;
        }
};

class CCirWin : public CShape
{
    protected :
        int radius;

    public :
        CCirWin(int r = 10)
        {
            radius = r;
        }

        virtual int area()
        {
            return (int) (3.14 * radius * radius);
        }

        void showArea()
        {
            cout << "The area of object CCirWin = " << area() << endl;
        }
};

int main(void)
{
    CWin win1(50, 60);
    CCirWin win2(100);

    win1.showArea();
    win2.showArea();

    system("pause");

    return 0;
}