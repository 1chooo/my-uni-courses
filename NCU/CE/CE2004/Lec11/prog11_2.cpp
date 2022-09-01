#include <iostream>
#include <cstdlib>

using namespace std;

struct myData
{
    string name;
    int math;
} student;

int main(void)
{
    cout << "sizeof(student)=" << sizeof(student) << endl;

    system("pause");

    return 0;
}