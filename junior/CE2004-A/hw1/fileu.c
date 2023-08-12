/*============ fileu.c ================*/
int a = 100;         // location 1
extern int t;        // location 2
int bar(int y) {     // location 3
    int x;           // location 4
    x=y+t;           // location 5
    return(x); 
}                    // location 6