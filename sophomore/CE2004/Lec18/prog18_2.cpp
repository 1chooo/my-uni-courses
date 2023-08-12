#include <fstream>
#include <iostream>
#include <cstdlib>

using namespace std;

int main(void)
{
    ofstream afile("./src/donkey.txt", ios::app);

    if (afile.is_open())
    {
        afile << "有一天我心血來潮騎著去趕集";

        cout << "String has written to the file..." << endl;
    }
    else
        cout << "Failure to open file..." << endl;

    afile.close();

    system("pause");

    return 0;
}