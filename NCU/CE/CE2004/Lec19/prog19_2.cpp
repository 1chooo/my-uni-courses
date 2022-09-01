#include <iostream>
#include <cstdlib>

using namespace std;

int main(void)
{
    int array[10];

    try
    {
        for (int i = 0; i <= 10; i++)
        {
            if (i > 9)
                throw "Index out of bound...";
            if (i * i > 60)
                throw i;
            else    array[i] = i * i;
        }
    }
    catch (const char *str)
    {
        cout << "Catch the exception " << str << endl;
    }
    catch (int i)
    {
        cout << "The square of " << i << " bigger than 60." << endl;
    }
    
    system("pause");

    return 0;
}