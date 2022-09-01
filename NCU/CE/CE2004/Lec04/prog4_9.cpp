#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int score;
    cout << "Input your score:";

    cin >> score;

    if ((score < 0) || (score > 100))
        cout << "Input error!!" << endl;

    if ((score < 60) && (score > 49))
        cout << "Make up exam!!" << endl;

    system("pause");

    return 0;
}