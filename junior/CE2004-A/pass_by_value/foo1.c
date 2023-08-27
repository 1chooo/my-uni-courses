#include <stdio.h>
#include <stdlib.h>

void f(int a, int b) {
  a = a + b;
  b = a - b;
  printf("in foo(), %d %d\n", a, b);
}

int main(void) {
  int a = 10;
  int b = 5;

  f(a, b);

  printf("in main() %d %d\n", a, b);

  return 0;
}