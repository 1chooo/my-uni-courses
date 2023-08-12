#include <stdio.h>          // location 11


int bar(int);
int foo();
int main() {
    int a=1, b=2, c=3;      // location 9

    printf("%d", bar(a));
    return bar(a);          // location 10
}
int bar(int x) { 
    int a, b, c;            // location 1
    printf("%d, %d, %d\n", a, b, c);
    c=x;                    // location 2
    b=x*9;                  // location 3
    a=foo();                // location 4
    return a;               // location 5
}
int foo() {
    int a=1, b=2, c;        // location 6
    c=a+b;                  // location 7
    return c;               // location 8
}