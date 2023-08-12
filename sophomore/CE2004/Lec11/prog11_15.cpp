#include <iostream>
#include <cstdlib>

using namespace std;

int main(void)
{
    enum myKey
    {
        left,
        right,
        middle
    } mouse;
    int key;

    do
    {
        cout << "Button press? (0)Left (1) Right (2)Middle: ";
        cin >> key;
    } while ((key > 2) || (key < 0));

    mouse = static_cast<myKey> (key);

    switch (mouse)
    {
        case left: cout << "Left Button Pressed!" << endl;
            break;
        case right: cout << "Right Button Pressed!" << endl;
            break;
        case middle: cout << "Middle Button Pressed!" << endl;
    }

    system("pause");

    return 0;
}