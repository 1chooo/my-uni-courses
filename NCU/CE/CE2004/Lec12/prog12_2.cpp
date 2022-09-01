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

    win1.id = 'A';
    win1.width = 50;
    win1.height = 40;

    cout << "Window " << win1.id << ":" << endl;
    cout << "win1.width = " << win1.width << endl;
    cout << "win1.height = " << win1.height << endl;

    system("pause");

    return 0; 
}