#include <iostream>
#include <cstdlib>

using namespace std;

class CWin
{
    public:
        void setData(char i, int w, int h)
        {
            id = i;
            width = w;
            height = h;
        }
    
    private:
        char id;
        int width;
        int height;

    friend void showMember(CWin);
};

void showMember(CWin w)
{
    cout << "Window " << w.id;
    cout << ": width = " << w.width;
    cout << ", height = " << w.height << endl;
}

int main(void)
{
    CWin win1, win2;

    win1.setData('A', 50, 40);
    win2.setData('B', 80, 60);

    showMember(win1);
    showMember(win2);

    system("pause");

    return 0;
}