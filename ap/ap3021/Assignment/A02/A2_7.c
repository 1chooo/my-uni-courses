#include <stdio.h>
#include <math.h>

double preAbs(double), machineEpsilon(void), IterMeth(double, double, double);

double preAbs(double x) {
  if (x < 0)
    x = -x;

  return x;
}

double machineEpsilon(void) {
  double epsilon = 1.0, xmin;

  while (epsilon > 0) {
    xmin = epsilon;
    epsilon = epsilon / 2;
  }

  return xmin;
}

double IterMeth(double val, double es, double maxit) {
  double iter = 0.0, sol = val, ea = 100.0, solold;

  while (1) {
    solold = sol;
    sol = (sol + val / sol) / 2;
    iter += 1.0;

    if (sol != 0)
      ea = preAbs((sol - solold) / sol) * 100;

    printf("%g %g\n", sol, ea);

    if ((ea <= es) || (iter >= maxit))
      break;
  }

  return sol;
}

int main() {
  double a;

  printf("Input a: ");
  scanf("%lf", &a);
  printf("%g", IterMeth(a, machineEpsilon(), 100));
  printf("\n");

  return 0;
}