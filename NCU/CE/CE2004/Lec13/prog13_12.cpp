#include <iostream>
#include <cstdlib>

using namespace std;

class CWin
{
    private :
        char id;
        int width, height;

    public :
        static int num;

        CWin(char i, int w, int h) : id(i), width(w), height(h)
        {
            num++;
        }

        CWin()
        {
            num++;
        }
};

int CWin::num = 0;

int main(void)
{
    CWin win1('A', 50, 40);
    CWin win2('B', 60, 80);

    cout << "We have built " << CWin::num << " objects." << endl;

    CWin myWin[4];
    cout << "We have built " << CWin::num << " objects." << endl;

    system("pause");

    return 0;
}