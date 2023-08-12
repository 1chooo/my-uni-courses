
#include <stdio.h>
double iterFact(int);
double recurFact(int);

int main()
{
  int n;
  printf("n:(>=0): ");
  scanf("%d", &n);
  while (n < 0)
  { /*error loop */
    printf("n:(>=0): ");
    scanf("%d", &n);
  }
  printf("%d factorial is %f.\n", n, iterFact(n));
  printf("%d factorial is %f.\n", n, recurFact(n));
}

double recurFact(int n)
{ /*recursive version */
  if ((n == 0) || (n == 1))
    return 1.0;
  return n * recurFact(n - 1);
}

double iterFact(int n)
{ /* find the factorial, return as a double
     to keep it from overflowing */
  int i;
  double answer;
  if ((n == 0) || (n == 1))
    return 1.0;
  answer = 1.0;
  for (i = n; i > 1; i--)
    answer *= i;
  return answer;
}