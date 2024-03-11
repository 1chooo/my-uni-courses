#include "stdio.h"

int fibonacci(int);
int recursiveFibonacci(int);

int fibonacci(int n) {
    if (n == 1 || n == 2) {
        return 1;
    } else {
        int a = 1;
        int b = 1;
        int c = 0;

        for (int i = 3; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }

        return c;
    }
}

int recursiveFibonacci(int n) {
    if (n == 1 || n == 2) {
        return 1;
    } else {
        int a = recursiveFibonacci(n - 1);
        int b = recursiveFibonacci(n - 2);
        return (a + b);
    }
}