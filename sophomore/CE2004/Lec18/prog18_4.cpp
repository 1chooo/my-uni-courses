#include <fstream>
#include <iostream>
#include <cstdlib>

using namespace std;

int main(void)
{
    char txt[] = "Welcome to the C++ world";
    int i = 0;

    ofstream ofile("./src/welcome.txt", ios::out);

    while (txt[i] != '\0')
    {
        ofile.put(txt[i]);
        i++;
    }

    cout << "Writing string success..." << endl;

    ofile.close();

    system("pause");

    return 0;
}