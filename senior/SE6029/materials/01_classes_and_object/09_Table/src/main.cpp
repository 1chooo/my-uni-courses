#include "Table.h"

void h() {
    Table t1;
    Table t2 = t1;
    Table t3;
    t3 = t2;
}

int main() {
    h();
    return 0;
}
