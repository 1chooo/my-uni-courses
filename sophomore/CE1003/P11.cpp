#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

int main ()
{

    while (1) {
        int size;
        int i;
        int pos;
        int count = 0;
        int setLength = 0;
        char a;
        char b;
        set<char> t1;

        cin >> size;
        if (size == -1) {
            cout << endl;
            break;
        }

        for (int i = 0 ; i < size; i++) {
            cin >> a;
            t1.insert(a);
        }

        for (set<char>::iterator i = t1.begin(); i != t1.end(); i++) {
            cout << *i << " ";
        }

        cout << endl;
        cin >> b;
        setLength = t1.size();
        vector<char> vect(t1.begin(),t1.end());
        for (int i = 0; i < setLength; i++) {
            if (b == vect[i]) {
                cout << i << endl;
                break;
            }
            else {
                count += 1;
            }
            if (setLength == 1 and count == 1) {
                cout << "-1" << endl;
            }
            else if(count == (setLength-1)) {
                cout << "-1" << endl;
            }
        }
        cout << endl;
    }

    return 0;
}