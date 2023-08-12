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
    CWin win1, win2;

    win1.id = 'A';
    win1.width = 50;
    win1.height = 40;

    win2.id = 'B';
    win2.width = win1.width + 20;
    win2.height = win1.height + 10;

    cout << "Window" << win2.id << ":" << endl;
    cout << "win2.width = " << win2.width << endl;
    cout << "win2.height = " << win2.height << endl;

    system("pause");

    return 0;
}