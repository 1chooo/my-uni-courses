#include <iostream>
#include <cstdlib>

using namespace std;

class CWin
{
    private:
        char id;
        int width;
        int height;

        int area(void)
        {
            return width * height;
        }
    
    public:
        void showArea(void)
        {
            cout << "Window " << id << ", area = " << area() << endl;
        }

        void setData(char i, int w, int h)
        {
            id = i;

            if (w > 0 && h > 0)
            {
                width = w;
                height = h;
            }
            else
                cout << "input error" << endl;
        }
};

int main(void)
{
    CWin win1;

    win1.setData('A', 50, 40);
    win1.showArea();

    system("pause");

    return 0;
}