#include <iostream>
#include <cstdlib>

using namespace std;

class CWin
{
    protected :
        char id;
        int width;
        int height;

    public :
        CWin(char ch, int w, int h) : id(ch), width(w), height(h)
        {}

        void show(void);
};

void CWin::show(void)
{
    cout << "Window " << id << ":" << endl;
    cout << "Area = " << width * height << endl;
}

int main(void)
{
    CWin win1('A', 50, 60);
    win1.show();

    system("pause");

    return 0;
}