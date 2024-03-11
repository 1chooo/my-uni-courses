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

        void count(void)
        {
            cout << "We have built " << num << " objects." << endl;
        }
};

int CWin::num = 0;

int main(void)
{
    CWin win1('A', 50, 40);
    CWin win2('B', 60, 80);

    win1.count();

    CWin myWin[4];

    win2.count();       // we can also call "count()" through win2

    system("pause");

    return 0;
}