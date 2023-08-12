#include <iostream>
#include <cstdlib>

using namespace std;

class CWin
{
    private :
        char id;
        int width, height;
        static int num;

    public :
        CWin(char i, int w, int h) : id(i), width(w), height(h)
        {
            num++;
        }

        CWin()
        {
            num++;
        }

        static void count(void)
        {
            cout << "We have built " << num << " objects..." << endl;
        }
};

int CWin::num = 0;

int main(void)
{
    CWin::count();

    CWin win1('A', 50, 40);
    CWin win2('B', 60, 80);

    CWin::count();

    CWin myWin[5];
    CWin::count();

    system("pause");

    return 0;
}