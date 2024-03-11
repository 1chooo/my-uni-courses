#include <iostream>
#include <string>

using namespace std;

int main ()
{
    while (1) {
        string input;
        int i, left, left1, right, right1, length;
        length = 0;

        cin >> input;
        if (input == "-1") {
            cout << endl;
            break;
        }

        for (i = 0; i < input.size(); i++) {
            if (input[i] == input[i + 1]) {
                left = i;
                right = i + 1;
                while (input[left] == input[right] && left >= 0) {
                    left--;
                    right++;
                }
                left++;
                right--;
                if (length < right - left + 1) {
                    length = right - left + 1;
                    left1 = left;
                    right1 = right;
                }
            }
            else if (input[i - 1] == input[i + 1] && (i - 1) >=0) {
                left = i - 1;
                right = i +1;
                while (input[left] == input[right] && left >= 0) {
                    left--;
                    right++;
                }
                left++;
                right--;
                if (length < right - left + 1) {
                    length = right - left + 1;
                    left1 = left;
                    right1 = right;
                }
            }
        }
        if (length != 0) {
            cout << "Palindrome: ";
            for (i = left1; i <= right1; i++) {
                cout << input[i];
            }
            cout << endl;
            cout << "length: " << length << endl << endl;
            length = 0;
        }
        else {
            cout << "Palindrome not existed!" << endl << endl;
        }
    }

    return 0 ;
}