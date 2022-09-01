//  It might be danger because of called data out of class.

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

        void showArea()
        {
            cout << "Window " << id;
            cout << ", area = " << area() << endl;
        }
};

int main(void)
{
    CWin win1;

    win1.id = 'A';
    win1.width = -50;
    win1.height = 40;
    win1.showArea();

    system("pause");

    return 0;
}