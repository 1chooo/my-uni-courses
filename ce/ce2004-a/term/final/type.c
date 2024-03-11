#include <stdio.h>

int main()
{
  float f;
  int i;

  i = 0.07;
  f = i; /*Location 1*/
  f = 3.57;
  i = f; /*Location 2*/

  return 0;
}