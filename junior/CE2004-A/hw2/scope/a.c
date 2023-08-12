/* file a.c */

#include <stdio.h>

static int i = 100;
extern int j;
extern int foo();

int main() {
  printf("main(): i=%d\n", i);
  printf("main(): j=%d\n", j);

  return foo();
}