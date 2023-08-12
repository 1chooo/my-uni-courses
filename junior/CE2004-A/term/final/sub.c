#include <stdio.h>

void fun1(void); /* Function prototype */
void fun2(void); /* Function prototype */
void fun3(void); /* Function prototype */

int main() {
    int a, b, c;
    
    /* Code in the main function */
    printf("Entering main function\n");
    
    a = 1;
    b = 2;
    c = 3;
    
    fun1(); /* Call fun1 function */
    
    printf("Exiting main function\n");
    return 0;
}

void fun1(void) {
    int b, c, d;
    
    /* Code in the fun1 function */
    printf("Entering fun1 function\n");
    
    b = 4;
    c = 5;
    d = 6;
    
    fun2(); /* Call fun2 function */
    
    printf("Exiting fun1 function\n");
}

void fun2(void) {
    int c, d, e;
    
    /* Code in the fun2 function */
    printf("Entering fun2 function\n");
    
    c = 7;
    d = 8;
    e = 9;
    
    fun3(); /* Call fun3 function */
    
    printf("Exiting fun2 function\n");
}

void fun3(void) {
    int d, e, f;
    
    /* Code in the fun3 function */
    printf("Entering fun3 function\n");
    
    d = 10;
    e = 11;
    f = 12;
    
    printf("Exiting fun3 function\n");
}

/*
This code defines three functions: 
fun1, fun2, and fun3. 
Each function has its own local variables. 
The main function serves as the entry 
point of the program. 
It declares variables a, b, and c and 
sequentially calls the fun1, fun2, and fun3 functions.

When running this code, each function 
will enter and execute its own code, 
and then return to the function that 
called it. You can observe the execution 
order of each function and the scope of 
local variables. Please note that the 
main function is called at the beginning 
of the program, and the fun3 function 
is the last function to be called.
*/