#include <iostream>
#include <cstdlib>

using namespace std;

union myData
{
    int score;
    char grade;
} student = {65};

int main(void)
{
    cout << "sizeof(student)=" << sizeof(student) << endl;
    cout << "student.score=" << student.score << endl;

    system("pause");

    return 0;
}