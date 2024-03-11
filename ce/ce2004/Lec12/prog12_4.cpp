#include <iostream>
#include <cstdlib>

using namespace std;

class CWin
{
    public:
        char id;
        int width;
        int height;
};

int main(void)
{
    CWin win1;

    cout << "sizeof(win1) = " << sizeof(win1) << "bytes" << endl;
    cout << "sizeof(CWin) = " << sizeof(CWin) << "bytes" << endl;

    system("pause");

    return 0;
}