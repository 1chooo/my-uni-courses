#include <iostream>
#include <cstdlib>

using namespace std;

class CWin
{
    private:
        char id;
        int width;
        int height;

    public:
        int area(void)
        {
            return width * height;
        }

        void showArea(void)
        {
            cout << "Window " << id << ", area = " << area() << endl;
        }
};

int main(void)
{
    CWin win1;

    /*
    This writing is wrong because we can't change private
    part directly.

    win1.id = 'A';
    win1.width = -5;
    win1.height = 12;
    */
    
    win1.showArea();

    system("pause");

    return 0;
}