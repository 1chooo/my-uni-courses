#include <iostream>
#include "new_cwin.h"

using namespace std;

class CMiniWin : public CWin
{
    public :
        CMiniWin(char ch, int w, int h) : CWin(ch, w, h)
        {}

        void show(void)
        {
            cout << "Mini window " << id << ":" << endl;
            cout << "Area = " << 0.8 * width * height << endl;
        }
};