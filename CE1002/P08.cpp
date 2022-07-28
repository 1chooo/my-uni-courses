#include <iostream>
#include <cmath>
#include <math.h>

using namespace std;

int main ()
{
    string n, i;
    float e, m, c, aa, wa;
    int we, wm, wc;

    cout << "Please input your name : ";
    cin >> n;
    cout << "Please input your student ID : ";
    cin >> i;
    cout << "English score : ";
    cin >> e;
    cout << "Math score : ";
    cin >> m;
    cout << "Chinese score : ";
    cin >> c;
    cout << "English weight : ";
    cin >> we;
    cout << "Math weight : ";
    cin >> wm;
    cout << "Chinese weight : ";
    cin >> wc;

    aa = (e + m + c) / 3;
    wa = ((e * we) + (m * wm) + (c * wc)) / (we + wm + wc);

    cout << endl << "Student name : "   << n
         << endl << "Student ID : "     << i
         << endl << "Arithmetic average : " << floor(aa)
         << endl << "Weighted average : "   << floor(wa)
         << endl;

    return 0;
}