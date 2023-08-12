#include <stdio.h>

int t;
int *p;

int main()
{
  int q;
  t = 987;
  p = &t;
  printf("Hello \n");   /* location 1 */

  return 0;
}