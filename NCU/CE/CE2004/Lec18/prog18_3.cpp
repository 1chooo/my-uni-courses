#include <fstream>
#include <iostream>
#include <cstdlib>

using namespace std;

int main(void)
{
    char txt[40];
    ifstream ifile("./src/donkey.txt", ios::in);

    while (!ifile.eof())
    {
        ifile >> txt;
        cout << txt << endl;
    }

    ifile.close();

    system("pause");

    return 0;
}