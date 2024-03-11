#include <stdio.h>
#include <stdlib.h>

void f(int x, int y) {
  int tmp = x;
  x = y;
  y = tmp;
}

int main(void) {
  int x = 3, y = 4;
  f(x, y);

  int v = (x - y) * (x + y) / 2;

  printf("%d\n", v);
  
  return 0;
}