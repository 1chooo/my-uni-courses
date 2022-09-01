#include <iostream>
#include <cstdlib>

using namespace std;

template <class T1, class T2>

class CWin
{
    protected :
        T1 width;
        T2 height;

    public :
        CWin(T1 w, T2 h) : width(w), height(h)
        {}

        void show(void);
};

template <class T1, class T2>

void CWin<T1, T2>::show()
{
    cout << "width = " << width << ", ";
    cout << "height = " << height << endl;
}

int main(void)
{
    CWin<int, double> win1(50, 60.05);
    CWin<double, int> win2(50.25, 74);

    cout << "win1 object: ";
    win1.show();
    cout << "win2 object: ";
    win2.show();

    system("pause");

    return 0;
}