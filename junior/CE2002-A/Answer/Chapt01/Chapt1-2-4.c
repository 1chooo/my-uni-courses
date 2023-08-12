#include <stdio.h>
int min(int, int);
#define TRUE 1
#define FALSE 0

int main()
{
  int x, y, z;
  printf("x: ");
  scanf("%d", &x);
  printf("y: ");
  scanf("%d", &y);
  printf("z: ");
  scanf("%d", &z);
  if (min(x, y) && min(x, z))
  { /*x is the smallest */
    printf("%d ", x);
    if (min(y, z))
      printf("%d %d\n", y, z);
    else
      printf("%d%d\n", z, y);
  }
  else if (min(y, x) && min(y, z))
  { /*y is the smallest */
    printf("%d ", y);
    if (min(x, z))
      printf("%d %d\n", x, z);
    else
      printf("%d%d\n", z, x);
  }
  else
  { /*z is the smallest */
    printf("%d ", z);
    if (min(x, y))
      printf("%d %d\n", x, y);
    else
      printf("%d%d\n", y, x);
  }
  else printf("%d %d %d\n", z, y, x);
}

int min(int a, int b)
{
  if (a < b)
    return TRUE;
  return FALSE;
}