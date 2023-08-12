#include <iostream>
#include <cstdlib>
#include <iomanip>

using namespace std;

typedef struct
{
    int hour;
    int minute;
    float second;
} myTime;

void subs(myTime t[]);

int main(void)
{
    int i;

    myTime t[3] = {{6, 24, 45.58f},
                   {3, 40, 17.43f}};
    cout << setfill('0');
    subs(t);

    for (i = 0; i < 3; i++)
    {
        cout << "t[" << i << "]=" << setw(2) << t[i].hour << ":";
        cout << setw(2) << t[i].minute << ":";
        cout << setw(5) << t[i].second << endl;
    }

    system("pause");

    return 0;
}

void subs(myTime t[])
{
    int count2 = 0, count3 = 0;

    t[2].second = t[0].second + t[1].second;
    while (t[2].second >= 60)
    {
        t[2].second -= 60;
        count3++;
    }

    t[2].minute = t[0].minute + t[1].minute + count3;
    while (t[2].minute >= 60)
    {
        t[2].minute -= 60;
        count2++;
    }

    t[2].hour = t[0].hour + t[1].hour + count2;

    return;
}