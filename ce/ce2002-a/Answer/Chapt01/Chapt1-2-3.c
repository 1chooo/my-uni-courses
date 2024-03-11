#include <stdio.h>
#include <math.h>
#include <string.h>

#define TRUE 1
#define FALSE 0
#define MAX_STRING 100
void truth_table(int);

int main()
{
  int n;
  printf("n:(>=0): ");
  scanf("%d", &n);
  while (n <= 0)
  { /*error loop */
    printf("n:(>=0): ");
    scanf("%d", &n);
  }
  truth_table(n);
}

void truth_table(int n)
{ /* generate a truth_table by transforming # of
     permutations into binary */
  int i, j, div, rem;
  char string[MAX_STRING];
  for (i = 0; i < pow(2, n); i++)
  { /*number of permutations or rows in the table */
    strcpy(string, "\0");
    div = i;
    for (j = n; j > 0; j--)
    { /*number of bits needed for each row*/
      rem = div % 2;
      div = div / 2;
      if (!rem)
        strcat(string, "FALSE ");
      else
        strcat(string, "TRUE  ");
    }
    printf("%s\n", string);
  }
}