#include <stdio.h>

int main()
{
  int a[10][10], b[10][10], c[10][10];
  int i, j;
  for (i = 0; i < 10; i++)
  {
    for (j = 0; j < 10; j++)
    {
      a[i][j] = 1;
      b[i][j] = 2;
      c[i][j] = 3;
    }
    b[17][9] = 4;  /*location 1*/
    b[17][16] = 5; /*location 2*/
    b[-3][7] = 6;  /*location 3*/
    b[-3][-6] = 7; /*location 4*/
  }

  return 0;
}