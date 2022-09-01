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

        void showArea(void)
        {
            cout << "Window " << id << ", area = " << area() << endl;
        }

        void setData(char i, int w, int h)
        {
            id = i;
            width = w;
            height = h;
        }

        void setData(char i)
        {
            id = i;
        }

        void setData(int w, int h)
        {
            width = w;
            height = h;
        }
};

int main(void)
{
    CWin win1, win2;

    win1.setData('A', 50, 40);
    win2.setData('B');
    win2.setData(80, 120);

    win1.showArea();
    win2.showArea();

    system("pause");

    return 0;
}