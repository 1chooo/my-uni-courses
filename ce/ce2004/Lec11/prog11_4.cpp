#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

struct myData
{
    string name;
    int age;
} x;

int main(void)
{
    struct myData y = {"Lilly Chen", 18};
    x = y;

    cout << "x.name=" << x.name << ", x.age=" << x.age << endl;
    cout << "y.name=" << y.name << ", y.age=" << y.age << endl;

    system("pause");

    return 0;
}