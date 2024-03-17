#include <iostream>

using namespace std;

class Table
{
    char *p;
    int sz;

public:
    Table(int s = 15)
    {
        p = new char[100];
        cout << "constructor" << endl;
    }
    ~Table()
    {
        delete[] p;
        cout << "destructor" << endl;
    }
};

void h()
{
    Table t1;
    Table t2 = t1;
    Table t3;
    t3 = t2;
}

int main()
{
    h();

    return 0;
}
