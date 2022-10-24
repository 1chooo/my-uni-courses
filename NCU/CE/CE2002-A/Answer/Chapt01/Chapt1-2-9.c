#include <stdio.h>
double recurBinom(int, int);
double iterBinom(int, int);
double recurFact(int n);

int main()
{
  int n, m;
  printf("n:(>=0): ");
  scanf("%d", &n);
  while (n < 0)
  { /*error loop */
    printf("n:(>=0): ");
    scanf("%d", &n);
  }
  printf("m:(>=0): ");
  scanf("%d", &m);
  while (m < 0)
  { /*error loop */
    printf("m:(>=0): ");
    scanf("%d", &m);
  }
  printf("n: %d m: %d Recursive Binomial coefficient is %f.\n", n, m, recurBinom(n, m));
  printf("n: %d m: %d Iterative Binomial coefficient is %f.\n", n, m, iterBinom(n, m));
}

double iterBinom(int n, int m)
{ /* defined as n!/(m! - (n-m)!)*/
  int i;
  double nFact, mFact, nMinusMFact;
  if (n == m)
    return 1;
  if ((n == 0) || (n == 1))
    nFact = 1;
  else
  {
    nFact = 1;
    for (i = n; i > 1; i--)
      nFact *= i;
  }
  if ((m == 0) || (m == 1))
    mFact = 1;
  else
  {
    mFact = 1;
    for (i = m; i > 1; i--)
      mFact *= i;
  }
  if (((n - m) == 0) || ((n - m) == 1))
    nMinusMFact = 1;
  else
  {
    nMinusMFact = 1;
    for (i = n - m; i > 1; i--)
      nMinusMFact *= i;
  }
  return nFact / (mFact * nMinusMFact);
}

double recurFact(int n)
{ /*recursive version */
  if ((n == 0) || (n == 1))
    return 1.0;
  return n * recurFact(n - 1);
}

double recurBinom(int n, int m)
{ /*recursive version */
  return recurFact(n) / (recurFact(m) * recurFact(n - m));
}