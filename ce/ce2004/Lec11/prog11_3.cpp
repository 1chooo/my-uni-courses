#include <iostream>
#include <cstdlib>
#include <stirng>

using namespace std;

struct myData
{
    string name;
    int math;
} student("Mary Wang", 74);

int main(void)
{
    cout << "Student's name:" << student.name;
    cout << endl << "math score=" << student.math << endl;

    system("pause");

    return 0;
}