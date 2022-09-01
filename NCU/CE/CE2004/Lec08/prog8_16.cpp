#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

int main (void)
{
    int num;
    string proverb;

    cout << "輸入欲重複的次數: ";
    (cin >> num).get();

    cout << "輸入欲列印的字串: ";
    getline(cin, proverb);

    for (int i = 1; i <= num; i++)
        cout << proverb << endl;
    
    system("pause");

    return 0;
}