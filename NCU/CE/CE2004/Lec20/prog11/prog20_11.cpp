#include <iostream>
#include <cstdlib>
#include "new_cwin.h"
#include "cminiwin.h"

using namespace std;

int main(void)
{
    CWin win1('A', 50, 60);
    CMiniWin mWin('M', 40, 50);

    win1.show();
    mWin.show();

    system("pause");

    return 0;
}