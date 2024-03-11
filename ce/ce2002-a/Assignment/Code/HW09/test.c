/* The short test to use i++ and ++i. */

#include "stdio.h"
#include "stdlib.h"

int main(void) {
  int i = 1;
  int s = 0;

  s = ++i;          // plus one first, then assign to s
  s = i++;          // assign to s, then plus one.

  printf("%d", s);

  return 0;
}