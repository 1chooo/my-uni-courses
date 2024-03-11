#include <stdio.h>

int add_three_items(int a, int b, int c) {
  int d;

  d = a + b + c;

  return d;
}

main() {
  int a, b, c, f;
  extern int add_three_items();

  a = 1;
  b = 2;
  c = 3;
  f = add_three_items(a, b, c);
}

// int main(void) {
//   int a, b, c, f;
//   extern int add_three_items();

//   a = 1;
//   b = 2;
//   c = 3;
//   f = add_three_items(a, b, c);

//   printf("%d\n", f);

//   return 0;
// }
