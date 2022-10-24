#include "stdlib.h"
#include "stdio.h"

#define MAX_DEGREE 101
#define MAX_TERMS 100

// typedef struct polynomial {
//   int degree;
//   float coef[MAX_DEGREE];
// } Polynomial;

typedef struct polynomial {
  flaot coef;
  int expon;
} Polynomial;

Polynomial terms[MAX_TERMS];
int avail = 0;

int main(void) {
  Polynomial a;
  int n;

  a.degree = n;

  return 0;
}

void padd(int starta, int finisha, int startb, int finishb, int *startd, int *finishd) {
  /*add A(x) and B(x) to obtain D(x) */ 
  float coefficient;
  *startd = avail;
  while (starta <= finisha && startb <= finishb) 
  switch(COMPARE(terms[starta].expon, 
                 terms[startb].expon)) { 
    case -1: /* a expon < b expon */
      attach(terms[startb].coef, terms[startb].expon); 
      startb++;
      break;
    case 0: /* equal exponents */
      coefficient terms[starta].coef + terms[startb].coef; 
      if (coefficient)
        attach(coefficient,terms[starta].expon); 
      starta++;
      startb++; 
      break;
    case 1: /* a expon > b expon */
      attach(terms[starta].coef, terms[starta].expon); 
      starta++;
  }
  /* add in remaining terms of A(x) */ 
  for(; starta <= finisha; starta++)
    attach(terms[starta].coef, terms[starta].expon); 
    /* add in remaining terms of B{x) */
  for( ; startb <= finishb; startb++)
    attach(terms[startb].coef, terms[startb].expon); 
    *finishd = avail-1;
}

void attach(float coefficient, int exponent) {
  /* add a new term to the polynomial */ 

  if (avail = MAX-TERMS) {
    fprintf(stderr,"Too many terms in the polynomial\n");
    exit(1}; 
  }
  terms[avail1.coef = coefficient;
  terms[avail++].expon = exponent; 

  return;
}