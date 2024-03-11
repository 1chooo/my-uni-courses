#include <iostream>

using namespace std;

int main ()
{
    int firstNumber, secondNumber, thirdNumber;
    firstNumber = 0;
    secondNumber = 0;
    thirdNumber = 0;

    cout << "Please key in first number: " << endl;
    cin >> firstNumber;
    cout << "Please key in second number: " << endl;
    cin >> secondNumber;
    cout << "Please key in third number: " << endl;
    cin >> thirdNumber;

    // 1 max
    if (firstNumber >= (secondNumber + thirdNumber)) {
        cout << "Not triangle" << endl;
    }
    else  {
        if (firstNumber * firstNumber == (secondNumber * secondNumber + thirdNumber * thirdNumber)) {
            cout << "Right triangle" << endl;
        }
        else if (secondNumber == thirdNumber) {
            if (firstNumber == secondNumber) {
                cout << "Regular triangle" << endl;
            }
            else {
                cout << "Isosceles triangle" << endl;
            }
        }
        else {
            cout << "Triangle" << endl;
        }
    }

    // 2 max
    if (secondNumber >= (firstNumber + thirdNumber)) {
        cout << "Not triangle" << endl;
    }
    else {
        if (secondNumber * secondNumber == (firstNumber * firstNumber + thirdNumber * thirdNumber)) {
            cout << "Right triangle" << endl;
        }
        else if (firstNumber == thirdNumber) {
            if (secondNumber == firstNumber) {
            }
            else {
                cout << "Isosceles triangle" << endl;
            }
        }
    }

    // 3 max
    if (thirdNumber >= (firstNumber + secondNumber)) {
        cout << "Not triangle" << endl;
    }
    else {
        if (thirdNumber * thirdNumber == (firstNumber * firstNumber + secondNumber * secondNumber)) {
            cout << "Right triangle" << endl;
        }
        else if (firstNumber == secondNumber) {
            if (thirdNumber == secondNumber) {
            }
            else {
                cout << "Isosceles triangle" << endl;
            }
        }
    }

    return 0;
}
