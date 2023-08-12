#include "stdio.h"
#include "math.h"

int primeCheck1(int);
int primeCheck2(int);

int primeCheck1(int n) {
    for (int i = 2; i < n; i++) {
        if (n % i == 0) {
            return 0;
        } 
    }
    return 1;
}

int primeCheck2(int n) {
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            return 0;
        } 
    }
    return 1; 
}