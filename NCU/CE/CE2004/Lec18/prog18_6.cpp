#include <fstream>
#include <iostream>
#include <cstdlib>
#include <cmath>

using namespace std;

int main(void)
{
    double num;
    ofstream ofile("./src/binary.dat", ios::binary);

    for (int i = 1; i <= 5; i++)
    {
        num = sqrt((double) i);
        ofile.write((char*) &num, sizeof(num));
    }

    cout << "Data have been written to the file with binary format." << endl;

    ofile.close();

    system("pause");

    return 0;
}