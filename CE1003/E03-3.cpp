#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>

using namespace std;

int main () {
    string input;
    set<char> t1;


    while (1) {

        getline(cin, input);

        if (input == "-1") {
            break;
        }

        string tmp;
        string str;
        int length;

        tmp = "";
        ifstream file(input, ios::in);

        while (file >> tmp) {
            str += tmp;
        }

        cout << str << endl;

        length = str.size();

        for (int i = 0; i < length; i++) {

            int count = 0;

            if (str[i] == '+' or str[i] == '-' or str[i] == '*' or str[i] == '/') {
                count = i;
            }
            if (count == 0) {
                cout << str[i] << endl;
            }

        }





    }


    return 0;
}
