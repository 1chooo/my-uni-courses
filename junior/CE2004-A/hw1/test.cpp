#include <stdio.h>

int main(void)
{

  int index = 10;

  while (--index)
  {
    int index = 10;
    printf("index is %d\n", index);
  }

  return 0;
}