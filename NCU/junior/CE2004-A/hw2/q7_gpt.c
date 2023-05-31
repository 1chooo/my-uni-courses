#include <stdio.h>

int main() {
    float a = 3.0, b = 2.0, c = 4.0;
    float expression1, expression2;

    expression1 = (a + b) * c;    // Expression 1: Addition followed by multiplication
    expression2 = a * c + b * c;  // Expression 2: Multiplication followed by addition

    printf("Expression 1: (a + b) * c = %f\n", expression1);
    printf("Expression 2: a * c + b * c = %f\n", expression2);

    return 0;
}

/*
Expression 1: (a + b) * c = 20.000000
Expression 2: a * c + b * c = 26.000000

In this program, we have two equivalent expressions: 
(a + b) * c and a * c + b * c. 
However, due to the difference in evaluation order, 
the results are different. 
Expression 1 first adds a and b, then multiplies the result by c, 
resulting in 20.0. Expression 2 first multiplies a by c, 
multiplies b by c, and finally adds the two products together, 
resulting in 26.0.
*/
