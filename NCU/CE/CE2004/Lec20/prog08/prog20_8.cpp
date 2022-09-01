#include <iostream>
#include <cstdlib>
#include "cwin.h"

using namespace std;

int main(void)
{
    CWin win1('A', 50, 60);
    win1.show();

    system("pause");

    return 0;
}