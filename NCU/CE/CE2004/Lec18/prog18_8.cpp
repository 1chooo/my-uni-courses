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
    st.getData();

    ofstream ofile("./src/student.dat", ios::binary);

    ofile.write((char*) &st, sizeof(st));

    cout << "Data have been written into file..." << endl;

    ofile.close();

    system("pause");

    return 0;
}