#include "stdio.h"
#include "stdlib.h"

int main(void) {
  int i, *pi;
  float f, *pf;

  pi = (int *) malloc(sizeof(int));
  /* 
    casts an int pointer to a float pointer.
    pf = (float *) pi;
  */
  pf = (float *) malloc(sizeof(float));

  *pi = 1024;
  *pf = 3.14;

  printf("an integer = %d, a float = %f\n", *pi, *pf);

  free(pi);
  free(pf);

  return 0;
}