#include <iostream>
#include <cstdlib>

using namespace std;

struct myData
{
    short math;
    float avg;
} student;

int main(void)
{
    cout << "sizeof(student)=" << sizeof(student) << endl;
    cout << "address of student.math=" << &student.math << endl;
    cout << "address of student.avg=" << &student.avg << endl;

    system("pause");

    return 0;
}