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
};

int main(void)
{
    CWin win1;

    win1.setData('B', 50, 40);
    win1.showArea();

    system("pause");

    return 0;
}