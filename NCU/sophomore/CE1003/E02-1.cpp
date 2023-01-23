#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main () {

    ifstream inputFile("N.txt");

    if (!inputFile) {
        cout << "File could not be opened!" << endl;
    }
    else {
        string tmp;

        tmp = "";

        while (inputFile >> tmp) {
            cout << tmp << endl;
        }

    }
    inputFile.close();





    return 0;
}