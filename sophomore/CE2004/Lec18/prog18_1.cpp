#include <fstream>
#include <iostream>
#include <cstdlib>

using namespace std;

int main(void)
{
    ofstream ofile("./src/donkey.txt", ios::out);

    if (ofile.is_open())
    {
        ofile << "我有一隻小毛驢" << endl;
        ofile << "我從來也不騎" << endl;

        cout << "String has written to the file..." << endl;
    }
    else
        cout << "Failure to open file..." << endl;

    ofile.close();

    system("pause");

    return 0;
}