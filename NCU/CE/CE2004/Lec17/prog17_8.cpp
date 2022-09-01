/*
 The wrong example of virtual function
 and deconstructor.
 */

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

        ~CShape()
        {
            cout << "The deconstructor ~CShape has been called..." << endl;

            system("pause"); 
        }
};

class CWin : public CShape
{
    protected : 
        int width, height;

    public :
        CWin(int w = 10, int h = 10) : width(w), height(h)
        {}

        virtual int area()
        {
            return width * height;
        }

        void showArea()
        {
            cout << "The area of object CWin = " << area() << endl;
        }

        ~CWin()
        {
            cout << "The deconstructor ~CWin() has been called..." << endl;

            system("pause");
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

        ~CMiniWin()
        {
            cout << "The deconstructor ~CMiniWin() has been called..." << endl;

            system("pause");
        }
};

int main(void)
{
    CShape *ptr = new CWin(50, 60);

    ptr -> showArea();
    cout << "Destroy object CWin..." << endl;

    delete ptr;

    cout << endl;

    ptr = new CMiniWin(50, 50);
    ptr -> showArea();
    cout << "Destroy object CMiniWin..." << endl;

    delete ptr;

    cout << endl;

    CMiniWin mWin(100, 100);
    mWin.showArea();

    system("pause");

    return 0;
}