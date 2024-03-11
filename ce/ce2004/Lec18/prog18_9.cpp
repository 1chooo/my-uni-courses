#include <fstream>
#include <iostream>
#include <cstdlib>

using namespace std;

class CStudent
{
    protected :
        char name[40];
        int age;

    public :
        void getData(void)
        {
            cout << "Enter name: ";
            cin >> name;
            cout << "Enter age: ";
            cin >> age;
        }

        void showData(void)
        {
            cout << "Name: " << name << endl;
            cout << "Age: " << age << endl;
        }
};

int main(void)
{
    CStudent st;
    ifstream ifile("./src/student.dat", ios::binary);

    ifile.read((char*) &st, sizeof(st));
    st.showData();

    ifile.close();

    system("pause");

    return 0;
}