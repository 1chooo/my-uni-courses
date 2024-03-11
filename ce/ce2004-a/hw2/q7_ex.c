#include <stdio.h>

#define SMALL_NUMBER_1 0.000007 
#define SMALL_NUMBER_2 0.000009

int main()
{
  float a, b, c, d, e;
  a = SMALL_NUMBER_1;
  b = c = SMALL_NUMBER_2;
  printf("a=%f\n", a);
  d = (a / (b * b * b * b * b * b * b * b * b * b));                 /*location 1*/
  e = (a / (b * b * b * b)) * (c / (b * b * b * b)) * (c / (b * b)); /*location 2*/
  d = d * c * c;                                                     /*location 3*/
  printf("(1)d = %f\n", d);                                          /*location 4*/
  printf("(2)e =%f\n", e);                                           /*location 5*/

  return 0;
}