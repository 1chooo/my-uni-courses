#include <iostream>

class Table {
private:
    int* p;
    int sz;
public:
    Table(int s = 15);
    Table(const Table &t);
    Table& operator=(const Table &t);
    ~Table();
};

Table::Table(int s) {
    p = new int[s];
    sz = s;
    std::cout << "constructor" << std::endl;
}

Table::Table(const Table &t) {
    p = new int[t.sz];
    sz = t.sz;
    for (int i = 0; i < sz; i++)
        p[i] = t.p[i];
}

Table& Table::operator=(const Table &t) {
    if (this != &t) {
        delete[] p;
        p = new int[t.sz];
        sz = t.sz;
        for (int i = 0; i < sz; i++)
            p[i] = t.p[i];
    }
    return *this;
}

Table::~Table() {
    delete[] p;
    std::cout << "destructor" << std::endl;
}

int main() {
    Table t1;
    Table t2 = t1;
    Table t3;
    t3 = t2;

    return 0;
}
