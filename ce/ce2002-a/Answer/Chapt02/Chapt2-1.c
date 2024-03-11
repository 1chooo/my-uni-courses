#include <stdio.h>
#include <stdlib.h>
int **make2dArray(int, int);

#define MALLOC(p, s)                        \
  if (!((p) = malloc(s)))                   \
  {                                         \
    fprintf(stderr, "Insufficient memory"); \
    exit(EXIT_FAILURE);                     \
  }

int main()
{
  int i, j;
  int **myArray;
  myArray = make2dArray(5, 10);
  myArray[2][4] = 6;
  for (i = 0; i < 5; i++)
  {
    for (j = 0; j < 10; j++)
    {
      /*myArray[i][j] =0;*/
      printf("%d ", myArray[i][j]);
    }
    printf("\n");
  }
}

int **make2dArray(int rows, int cols)
{ /*create a 2-d array rows x cols */
  int **x, i;
  MALLOC(x, rows * sizeof(*x)); /*get memory  for row pointers*/
  for (i = 0; i < rows; i++)
  {
    MALLOC(x[i], cols * sizeof(**x)); /*get memory for col pointers*/
    *x[i] = 0;
  }
  return x;
}