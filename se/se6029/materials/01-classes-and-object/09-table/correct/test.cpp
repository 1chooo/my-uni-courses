#include <iostream>
using namespace std;

// 絕大部分的情況下
// 「copy」 operator 與
// 「=」 operator 有很大的不同

// 根本的原因

//  copy operator 會初始化一塊未經初始化的記憶體
// 而 = operator 必須妥善處理一個已經建構好的的物件


class Table
{
    Table(const Table &);
    Table &operator=(const Table &);
};
Table :: Table(const Table &t)
{
    p = new Name[sz = t.sz];
    for (int i = 0; i < sz; i++)
        p[i] = t.p[i];
}
Table &Table :: operator=(const Table & t)
{
    if (this ! = &t)
    {
        delete[];
        p = new Name[sz = t.sz];
        for (int i = 0; i < sz; i++)
            p[i] = t.p[i];
    }
    return *this;
}
