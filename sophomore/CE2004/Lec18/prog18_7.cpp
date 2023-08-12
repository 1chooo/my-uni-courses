#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(void)
{
    ifstream ifile("./src/binary.dat", ios::binary);
    double num;

    for (int i = 1; i <= 5; i++)
    {
        ifile.read((char*) &num, sizeof(num));
        cout << num << endl;
    }

    cout << "The binary file has been read..." << endl;

    ifile.close();

    system("pause");

    return 0;
}