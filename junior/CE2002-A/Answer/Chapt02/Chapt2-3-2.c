void pmult(polynomial a[], polynomial b[], polynomial c[], int na, int nb, int *nc)
{ /*multiply two polynomials */
  int i, j;
  *nc = 0;
  for (i = 0; i < na; i++)
    for (j = 0; j < nb; j++)
    {
      c[*nc].coef = a[i].coef * b[j].coef;
      c[(*nc)++].expon = a[i].expon + b[j].expon;
    }
  /*put simplification here if you wish */
}