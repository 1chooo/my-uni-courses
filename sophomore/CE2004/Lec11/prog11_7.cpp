#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

struct data
{
    string name;
    int a, b;
};

void change(struct data *), prnstr(struct data);

int main(void)
{
    struct data first = {"David Young", 9, 2};

    prnstr(first);
    cout << "After process..." << endl;

    change(&first);
    prnstr(first);

    system("pause");

    return 0;
}

void change(struct data *ptr)
{
    int temp;
    
    temp = ptr->a;      // ptr->a means take out the value of ptr point to a
    ptr->a = ptr->b;
    ptr->b = temp;

    return;
}

void prnstr(struct data in)
{
    cout << "name=" << in.name << endl;
    cout << "a=" << in.a << "\t";
    cout << "b=" << in.b << endl;

    return;
}