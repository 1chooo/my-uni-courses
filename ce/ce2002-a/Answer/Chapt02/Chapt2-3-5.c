#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define MAX_TERMS 100
#define MAX_POLYS 15
typedef struct
{
  float coef;
  int expon;
} polynomial;

void readPoly(polynomial[][MAX_TERMS], int[], int *);
void printPoly(polynomial[], int);

int main()
{
  float x;
  polynomial terms[MAX_POLYS][MAX_TERMS];
  int nes[MAX_POLYS];
  int totalPolys = 0;
  readPoly(terms, nes, &totalPolys);
  readPoly(terms, nes, &totalPolys);
  printPoly(terms[0], nes[0]);
  printPoly(terms[1], nes[1]);
}

void printPoly(polynomial terms[], int n)
{ /*print the polynomial*/
  int i;
  for (i = 0; i < n - 1; i++)
    printf("%5.2fx^%d +", terms[i].coef, terms[i].expon);
  printf("%5.2fx^%d\n", terms[n - 1].coef, terms[n - 1].expon);
}

void readPoly(polynomial terms[][MAX_TERMS], int nes[], int *total)
{ /*read in a polynomial*/
  int i, expon, nterms;
  float coef;
  printf("Enter the number of terms in your polynomial: ");
  scanf("%d", &nterms);
  while (nterms >= MAX_TERMS)
  {
    printf("Too many terms in the polynomial\n");
    printf("Number of terms: ");
    scanf("%d", &nterms);
  }
  for (i = 0; i < nterms; i++)
  {
    printf("Coefficient: ");
    scanf("%f", &coef);
    printf("Exponent: ");
    scanf("%d", &expon);
    terms[*total][i].coef = coef;
    terms[*total][i].expon = expon;
  }
  nes[*total] = nterms;
  (*total)++;
}