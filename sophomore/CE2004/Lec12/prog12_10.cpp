#include <iostream>
#include <cstdlib>

using namespace std;

class CWin
{
    public:
        char id;
        int width;
        int height;

        int area()
        {
            return width * height;
        }

        void setData(char i, int w, int h)
        {
            id = i;
            width = w;
            height = h;
        }
};

void showArea(CWin win)
{
    cout << "Window " << win.id << ", area = " << win.area() << endl;
}

int main(void)
{
    CWin win1;

    win1.setData('B', 50, 40);
    showArea(win1);

    system("pause");

    return 0;
}