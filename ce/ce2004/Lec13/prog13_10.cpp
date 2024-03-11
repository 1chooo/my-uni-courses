#include <iostream>
#include <cstdlib>

using namespace std;

class CWin
{
    private :
        char id;
        int width, height;

    public :
        void setMember(char i, int w, int h)
        {
            id = i;
            width = w;
            height = h;
        }

        int area(void)
        {
            return width * height;
        }

        friend void largest(CWin [], int);
};

void largest(CWin win[], int n)
{
    int max = 0, iw;

    for (int i = 0; i < n; i++)
        if (win[i].area() > max)
        {
            iw = i;
            max = win[i].area();
        }

    cout << "largest window = " << win[iw].id << endl;
}

int main(void)
{
    CWin win[3];

    win[0].setMember('A', 60, 70);
    win[1].setMember('B', 40, 60);
    win[2].setMember('C', 80, 50);

    largest(win, 3);

    system("pause");

    return 0;
}