/*============ filev.c ================*/
#include<stdio.h>
int t=9;                            // location 7
extern int a;                       // location 8
extern int bar(int);                // location 9
int main(){                         // location 10
    int z;                          // location 11
    printf("a=%d\n", a);
    printf("bar(3)=%d\n",bar(3));
}                                   // location 12