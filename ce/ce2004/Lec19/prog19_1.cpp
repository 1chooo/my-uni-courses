#include <iostream>
#include <cstdlib>

using namespace std;

int main(void)
{
    int array[5];

    try
    {
        for (int i = 0; i <= 10; i++)
        {
            if (i >= 5)
                throw "Index out of bound...";
            else
            {
                array[i] = i * i;
                cout << "array[" << i << "] = " << array[i] << endl;
            }
        }
    }
    catch (const char *str)
    {
        cout << "Catch the exception: " << str << endl;
    }

    system("pause");

    return 0;
}