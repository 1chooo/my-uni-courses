#include <iostream>
#include <cstdlib>
#include <cmath>

using namespace std;

bool primeCheck1(int);
bool primeCheck2(int);

bool primeCheck1(int n) {
    for (int i = 2; i < n; i++) {
        if (n % i == 0) {
            return false;
        } 
    }
    return true;
}

bool primeCheck2(int n) {
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            return false;
        } 
    }
    return true; 
}