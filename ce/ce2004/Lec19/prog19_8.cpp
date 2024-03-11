#include <iostream>
#include <cstdlib>

using namespace std;

template <class T>

class CWin
{
    protected :
        T width, height;

    public :
        CWin(T w, T h) : width(w), height(h)
        {}

        void show(void);
};

template <class T>

void CWin<T>::show()
{
    cout << "width = " << width << ", ";
    cout << "height = " << height << endl;
}

int main(void)
{
    CWin<int> win1(50, 60);
    CWin<double> win2(50.25, 60.74);

    cout << "win1 object: ";
    win1.show();
    cout << "win2 object: ";
    win2.show();

    system("pause");

    return 0;
}