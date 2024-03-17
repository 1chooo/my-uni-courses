# Copy constructor and `=` operator

```cpp
#include <iostream>
using namespace std;
class Table
{
    char *p;
    int sz;

public:
    Table(int s = 15)
    {
        p = new char[100];
        cout << "constructor" << endl;
    }
    ~Table()
    {
        delete[] p;
        cout << "destructor" << endl;
    }
};
void h()
{
    Table t1;
    Table t2 = t1;
    Table t3;
    t3 = t2;
}
int main()
{
    h();

    return 0;
}
```

- How many times the default constructor is called? 請問Table預設的建構式被呼叫了幾次？

- How many times the default destructor is called ? (Table 的解構式被呼叫了幾次？)

- What is the final output?


