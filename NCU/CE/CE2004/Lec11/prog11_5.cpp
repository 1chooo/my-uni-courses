#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

struct myData
{
    string name;
    int age;
};

void func(struct myData);

int main(void)
{
    struct myData woman = {"Mary Wu", 5};

    cout << "Before process..." << endl;
    cout << "In main(), " << woman.name;
    cout << "'s age is " << woman.age << endl;

    cout << "After process..." << endl;
    func(woman);
    cout << "In main(), " << woman.name;
    cout << "'s age is " << woman.age << endl;

    system("pause");

    return 0;
}

void func(struct myData a)
{
    a.age += 10;
    cout << "In func(), " << a.name;
    cout << "'s age is " << a.age << endl;

    return;
}