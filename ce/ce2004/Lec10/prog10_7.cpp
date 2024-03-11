#include <iostream>
#include <cstdlib>

using namespace std;

char *setString(char *);

int main(void)
{
    char *str;

    str = setString("Hello C++!");
    cout << str << endl;

    delete[] str;

    system("pause");

    return 0;
}

char *setString(char *text)
{
    char *ptr;

    ptr = new char[strlen(text) + 1];
    strcpy(ptr, text);

    return ptr;
}