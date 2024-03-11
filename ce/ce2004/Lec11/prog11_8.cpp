#include <iostream>
#include <cstdlib>

using namespace std;

union myData
{
    char grade;
    int score;
} student;

int main(void)
{
    char sex;

    do {
        cout << "Your sex is (1)Male (2) Female:";
        cin.get(sex);
        cin.get();
    } while ((sex > 50) || (sex < 49));

    if (sex == '1')
    {
        cout << "Input score:";
        cin >> student.score;
    } 
    else 
    {
        cout << "Input grade:";
        cin.get(student.grade);
    }

    cout << "**** output ****" << endl;

    if (sex == '1')
        cout << "student.score=" << student.score << endl;
    else
        cout << "student.grade=" << student.grade << endl;

    system("pause");

    return 0;
}