#include <stdio.h>
#include <math.h>
double f(double x)
{
  double y;
  y = pow(x, 10.0) - 1;
  return y;
}

double a(double x)
{
  if (x < 0)
    x = -x;
  return x;
}

double ModFalsePos(double xl, double xu, double es, int imax)
{
  double xr = xu + 1, xold; // avoid the xr in the first iteration being equal to xold
  double ea, test, et;
  int iter = 0, iu = 0, il = 0;
  double fl = f(xl), fu = f(xu), fr;
  printf("iteration  %5s%12s%12s%12s%10s%10s\n", "xl", "xu", "xr", "f(xr)", "ea", "et");
  printf("_____________________________________________________________\n");
  while (1)
  {
    xold = xr;
    xr = xu - (f(xl - xu)) / (fl - fu); //(5.7)
    fr = f(xr);
    iter++;
    if (xr != 0)
      ea = a((xr - xold) / xr) * 100; // approximate error
    et = (1 - xr) / 1100;           // true error
    printf("%4d %12.10g %12.10g %12.10g %10g %10g %10g\n", iter, xl, xu, xr, fr, ea, et);
    // determine the part of the interval which contains the root
    test = fl * fr;
    if (test < 0)
    {
      xu = xr;
      fu = fr;
      iu = 0;
      il++;
      if (il >= 2)
        fl /= 2;
    }
    else if (test > 0)
    {
      xl = xr;
      fl = fr;
      il = 0;
      iu++;
      if (iu >= 2)
        fu /= 2;
    }
    else
      ea = 0.0; // test=0 implies f(xr)=0
    if (ea < es || iter >= imax)
      break;
  }
  return xr;
}

int main()
{
  double xl, xu, xr, es;
  int imax;
  printf("xl=");
  scanf("%lf", &xl);
  printf("xu=");
  scanf("%lf", &xu);
  printf("es=");
  scanf("%lf", &es);
  printf("imax=");
  scanf("%d", &imax);

  ModFalsePos(xl, xu, es, imax);

  return 0;
}