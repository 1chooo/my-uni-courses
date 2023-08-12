#include <iostream>
#include <cstdlib>

using namespace std;

int main (void)
{
    int i;
    cout << "Input an integer:";

    cin >> i;

    if (i > 5) 
        cout << i << " > 5 is correct." << endl;

    if (i % 2 == 0)
        cout << i << " is even." << endl;
        
    if (true)
        cout << "This line will always be conducted." << endl;
    
    system("pause");

    return 0;
}