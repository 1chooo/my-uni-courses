#ifndef TABLE_H
#define TABLE_H

class Table {
private:
    char* p;
    int sz;
public:
    Table(int s = 15);
    ~Table();
};

#endif /* TABLE_H */
