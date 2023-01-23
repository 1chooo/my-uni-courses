#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

struct myData
{
    string name;
    int math;
    int eng;
};

float avg(int, int);

int main(void)
{
    struct myData num = {"Alice", 71, 80};

    cout << num.name << "'s Math score=" << num.math;
    cout << endl << "English's score=" << num.eng << endl;
    cout << "average=" << avg(num.math, num.eng) << endl;

    system("pause");

    return 0;
}

float avg(int a, int b)
{
    return (float) (a + b) / 2;
}