/*
 To correct the wrong in prog17_4.cpp
 */

#include <iostream>
#include <cstdlib>

using namespace std;

class CWin
{
    protected :
        char id;
        int width, height;

    public :
        CWin(char i = 'D', int w = 10, int h = 10)
        {
            id = i;
            width = w;
            height = h;
        }

        void showArea()
        {
            cout << "Window " << id << ", area = " << area() << endl;
        }

        virtual int area()
        {
            return width * height;
        }
};

class CMiniWin : public CWin
{
    public :
        CMiniWin(char i, int w, int h) : CWin(i, w, h)
        {}

        virtual int area()
        {
            return (int) (0.8 * width * height);
        }
};

int main(void)
{
    CWin *ptr = new CWin('A', 70, 80);
    CMiniWin mWin('B', 50, 60);

    ptr -> showArea();
    delete ptr;

    ptr = &mWin;
    ptr -> showArea();

    system("pause");

    return 0;
}