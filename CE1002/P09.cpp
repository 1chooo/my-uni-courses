#include <iostream>
#include <string>

using namespace std;

int main ()
{
    int n;
    int i;
    int inputNumber;
    int count;
    int inputStringlen;
    string inputString;

    count = 1;

    cin >> inputNumber;

    for (int n = 0; n < (inputNumber + 1); n++) {
        count = 1;
        getline(cin, inputString);
        inputStringlen = inputString.length();

        for (int i = 1; i < inputStringlen; i++) {
            if (inputString[i] == inputString[i - 1]) {
                count += 1;
            }
            else {
                cout << inputString[i - 1] << count;
                count = 1;
            }

            if (i == (inputStringlen - 1)) {
                cout << inputString[i] << count << endl;
            }
        }
    }
    return 0;
}
