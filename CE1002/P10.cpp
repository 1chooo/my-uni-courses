#include <iostream>
#include <string>

using namespace std;

int main () {

    string input;

    while (input != "-1") {

        cin >> input;
        if (input == "-1") {
            break;
        }
        else if (input == string(input.rbegin(), input.rend())) {
            cout << "Palindrome!" << endl;
        }
        else {
            cout << "Not Palindrome!" << endl;
        }
    }

    return 0;
}