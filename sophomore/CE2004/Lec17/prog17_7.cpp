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

        void showArea()
        {
            cout << "The area of object CWin = " << area() << endl;
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

class CMiniWin : public CWin
{
    public :
        CMiniWin(int w, int h) : CWin(w, h)
        {}

        virtual int area()
        {
            return (int) (0.5 * width * height);
        }

        void showArea()
        {
            cout << "The area of object CMiniWin = " << area() << endl;
        }
};

int main(void)
{
    CWin win1(50, 60);
    CCirWin win2(100);
    CMiniWin win3(50, 60);

    win1.showArea();
    win2.showArea();
    win3.showArea();

    system("pause");

    return 0;
}