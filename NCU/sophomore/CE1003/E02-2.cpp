#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main () {
    ifstream inputFile("input.txt");


    if (!inputFile) {
        cout << "File could not be opened!" << endl;
    }
    else {
        string tmp;
        string str;

        tmp = "";

        while (getline(inputFile, tmp)) {
            str += tmp;
        }
        cout << str;

    }




    inputFile.close();
}