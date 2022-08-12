#include <iostream>
#include <string>

using namespace std;

int main () {
    int stack[100];
    string control;
    char input;
    int stackIndex;

    stackIndex = 0;

    while (1) {
        cin >> control;

        if (control == "push") {
            cin >> input;
            stack[stackIndex] = static_cast< int >(input);
            stackIndex++;
        }
        else if (control == "pop") {
            if (stackIndex == 0) {
                cout << "empty" << endl;
            }
            else {
                cout << static_cast< char > (stack[stackIndex - 1]) << endl;
                stackIndex--;
            }
        }
        else if (control == "list") {
            for (int i = 0; i < stackIndex; i++) {
                cout << static_cast< char >(stack[i]) << " ";
            }
            cout << endl;
        }
        else {
            cout << endl;
            break;
        }
    }
}