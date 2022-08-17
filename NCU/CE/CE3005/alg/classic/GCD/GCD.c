#include "stdio.h"

int EuclidGCD(int m, int n) {
	int r = m % n;

	while(r != 0) {
		m = n;
		n = r;
		r = m % n;
	}

	return n;	
}
