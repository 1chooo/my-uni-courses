#include "stdlib.h"
#include "stdio.h"

#define MAX_SIZE 100

float sum(float [], int);
void print1(int *, int);

int main(void) {
  float input[MAX_SIZE], answer;
  int i;
  
  for (i = 0; i < MAX_SIZE; i++) {
    input[i] = i;
  }

  answer = sum(input, MAX_SIZE);
  printf("The sum is: %f\n", answer);

  

  return 0;
}

float sum(float list[], int n) {
  int i;
  float tempSum = 0;

  for (i = 0; i < n; i++) {
    tempSum += list[i];
  }

  return tempSum;
}

void print1(int *ptr, int rows) {
  /* print out a one-dimensional array using a pointer. */

  int i;

  printf("Address Contents\n");

  for (i = 0; i < rows; i++) {
    printf("%8u%5d\n", ptr + i, *(ptr + i));
  }

  printf("\n");

  return;
}