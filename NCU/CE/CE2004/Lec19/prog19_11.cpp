#include <iostream>
#include <cstdlib>

using namespace std;

template <class T>

class CWin
{
    T width, height;

    public :
        CWin(T w, T h) : width(w), height(h)
        {}

        T area(void)
        {
            return width * height;
        }
};

template <> class CWin<int>
{
    int width, height;

    public :
        CWin(int w, int h) : width(w), height(h)
        {}

        int area(void)
        {
            return 0;
        }
};

int main(void)
{
    CWin<int> win1(50, 60);
    CWin<double> win2(12.3, 45.8);
    CWin<short> win3(12, 45);

    cout << "win1 object: ";
    cout << win1.area() << endl;

    cout << "win2 object: ";
    cout << win2.area() << endl;

    cout << "win3 object: ";
    cout << win3.area() << endl;

    system("pause");

    return 0;
}