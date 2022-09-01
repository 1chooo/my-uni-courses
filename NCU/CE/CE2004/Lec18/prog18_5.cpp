#include <fstream>
#include <iostream>
#include <cstdlib>

using namespace std;

int main(void)
{
    char txt[80], ch;

    ifstream ifile1("./src/welcome.txt", ios::in);
    ofstream ofile("./src/welcome2.txt", ios::out);

    while (ifile1.get(ch))
        ofile.put(ch);
    
    cout << "Finfish duplication..." << endl;

    ifile1.close();
    ofile.close();

    ifstream ifile2("./src/welcome2.txt", ios::in);

    while (!ifile2.eof())
    {
        ifile2.getline(txt, 80, '\n');
        cout << txt << endl;
    }

    ifile2.close();

    system("pause");

    return 0;
}